#!/usr/bin/env python3
# coding: utf-8
# vim: ts=4 sw=4 sts=4 expandtab

#
# by ganadist
# see https://gist.github.com/ganadist/de618f92897144273586648bc07cfd7b
#

import os, sys
import collections
import getopt
import imp
import resource
import select
import shutil
import signal
import tempfile
import time
import logging as L


def random_wrapper(*args, **kwd):
    assert False, 'random function called'


def install_random_wrapper():
    """ random 함수를 사용하면 assert 발생"""
    import random
    os.urandom = random_wrapper

    for sym in random.__all__:
        m = getattr(random, sym)
        if callable(m):
            setattr(random, sym, random_wrapper)


GAWI = 'gawi'
BAWI = 'bawi'
BO = 'bo'

WIN_TABLE = {
    BAWI: GAWI,
    GAWI: BO,
    BO: BAWI,
}

VALID_HANDS = WIN_TABLE.keys()


# child side
class TimeCheck(object):
    def __init__(self, timeout):
        self.timeout = timeout

    def gettime(self):
        # return resource.getrusage(resource.RUSAGE_SELF).ru_utime // 1000
        return time.time() * 1000

    def __enter__(self):
        self.start = self.gettime()

    def __exit__(self, type, value, tb):
        self.end = self.gettime()
        if self.timeout < self.end - self.start:
            assert False, 'timed out: {} actual:{}'.format(self.timeout, self.end - self.start)


class PlayerWrapper(object):
    def __init__(self, sourcefile, timeout):
        # install_random_wrapper()
        module = imp.load_source("player", sourcefile)
        self.func = getattr(module, 'show_me_the_hand')
        self.timeout = timeout

    def show_me_the_hand(self, records):
        with TimeCheck(self.timeout) as t:
            hand = self.func(records)
            assert hand in VALID_HANDS, 'invalid hand: {}'.format(repr(hand))
            return hand


# parent side
class PlayerException(Exception):
    def __init__(self, player, *arg):
        Exception.__init__(self, *arg)
        self.player = player


class TimeoutException(Exception):
    pass


class BrokenPipeException(Exception):
    pass


class SourceWrapper(tempfile.TemporaryDirectory):
    """ 임시 디렉토리를 만들고 소스를 복사하고 현재디렉토리를 module path에서
    제거하여, 다른 사람의 소스를 참고할 수 없게 한다"""

    def __init__(self, src):
        tempfile.TemporaryDirectory.__init__(self)
        self.src = os.path.abspath(src)

    def __enter__(self):
        wd = os.getcwd()
        if wd in sys.path:
            sys.path.remove(wd)
        tempname = tempfile.TemporaryDirectory.__enter__(self)
        os.chdir(tempname)
        dst = os.path.join(tempname, os.path.basename(self.src))
        shutil.copy(self.src, dst)
        return dst


class PlayerStub(object):
    """pipe를 이용해서 hand와 결과를 전달한다."""

    def __init__(self, sourcename, timeout, records=[]):
        self.sourcename = sourcename
        self.timeout = timeout
        self.records = records
        self.pid = 0
        self.spawn()

    def stop(self):
        L.debug('stop %s' % self.sourcename)
        if self.pid > 0:
            cpid, exit_code = os.wait()
            # L.debug('wait child pid=%d, exit_code=%d' % (cpid, exit_code))

    def spawn(self):
        self.wpipe = Pipe(self.timeout)
        self.rpipe = Pipe(self.timeout)
        self.pid = os.fork()
        if self.pid == 0:
            # child
            try:
                # L.debug('child %s fork' % self.sourcename)
                with SourceWrapper(self.sourcename) as src:
                    self.wrapper = PlayerWrapper(src, self.timeout)
                    # 래퍼를 통해 show_me_the_hand 를 실행하고...
                    h = self.wrapper.show_me_the_hand(self.records)
                    # L.debug('child %s hand %s' % (self.sourcename, h))
                    while True:
                        try:
                            # 선택한 손을 parent에 파이프로 전달
                            self.rpipe.writeline(h)
                            # parent가 파이프로 전달하는 대결 결과를 읽음
                            hand, result = self.wpipe.readline()[:-1].split()
                            # L.debug('child %s result: %s %s' % (self.sourcename, hand, result))
                        except:
                            # L.debug('child %s close', self.sourcename)
                            break
                        # 방금 대결 결과를 전체 기록에 누적...
                        self.records.insert(0, (hand, int(result)))
                        # 래퍼를 통해 show_me_the_hand 를 실행하고...
                        h = self.wrapper.show_me_the_hand(self.records)
                        # L.debug('child %s hand %s (cont.)' % (self.sourcename, h))
                L.debug('child %s exit' % self.sourcename)
            except Exception as e:
                # L.error('unknown error %r in child %s' % (e, self.sourcename))
                pass
            self.wpipe = self.rpipe = None
            sys.exit(0)
        elif self.pid > 0:
            # parent
            pass
        else:
            # error
            assert False, 'os.fork failed'

    def get_hand(self):
        try:
            return self.rpipe.readline()[:-1]
        except TimeoutException:
            raise PlayerException(self, 'timeout')
        except BrokenPipeException:
            raise PlayerException(self, 'broken pipe')
        except Exception as e:
            raise PlayerException(self, str(e))

    def send_result(self, hand, result):
        self.wpipe.writeline('\t'.join((hand, str(result))))

    def __del__(self):
        if self.pid > 0:
            self.wpipe = self.rpipe = None
            try:
                os.kill(self.pid, signal.SIGINT)
                os.waitpid(self.pid, 0)
            except:
                pass


class Pipe(object):
    """ 간단한 pipe 구현. timeout안에 read할 수 없으면 TimeoutException 발생"""

    def __init__(self, timeout):
        self.fd = os.pipe()
        self.timeout = timeout
        self.poller = select.poll()
        self.poller.register(self.fd[0], select.POLLIN | select.POLLHUP | select.POLLERR)

    def writeline(self, line):
        line += '\n'
        os.write(self.fd[1], line.encode('utf-8'))
        # os.fsync(self.fd[1])

    def readline(self):
        events = self.poller.poll(self.timeout)
        if not events:
            raise TimeoutException()
        for fd, flag in events:
            if flag & (select.POLLHUP | select.POLLERR):
                raise BrokenPipeException()
        return os.read(self.fd[0], 1024).decode('utf-8')

    def __del__(self):
        for fd in self.fd:
            os.close(fd)


def print_help():
    print('Usage: run [-t timeout] [-c count] source1 source2')


def fight(source1, source2, count, timeout):
    player1 = PlayerStub(source1, timeout)
    player2 = PlayerStub(source2, timeout)

    # List of Tuple(h1, h2, r)
    result = []
    for i in range(count):
        try:
            h1 = player1.get_hand()
            h2 = player2.get_hand()

            if h1 == h2:
                r = 0
            elif h2 == WIN_TABLE[h1]:
                r = 1
            else:
                r = -1

            player1.send_result(h2, -r)
            player2.send_result(h1, r)
            result.append((h1, h2, r))
        except PlayerException as e:
            if e.player is player1:
                print('player1 has exception:', e)
            else:
                print('player2 has exception:', e)
            break
            # sys.exit(0)

    return result


def print_result(p1, p2, result):
    counter = collections.Counter(map(lambda r: r[2], result))
    print('player1 %s win:%d draw:%d, lose:%d' % (p1, counter[1], counter[0], counter[-1]))
    print('player2 %s win:%d draw:%d, lose:%d' % (p2, counter[-1], counter[0], counter[1]))
    print('player1 records:', list(map(lambda r: (r[0], r[2]), result)))
    print('player2 records:', list(map(lambda r: (r[1], r[2]), result)))


if __name__ == '__main__':
    L.basicConfig(level=L.DEBUG)
    timeout = 1000
    count = 100
    opts, args = getopt.getopt(sys.argv[1:], 't:c:h', ["timeout", "count", "help"])
    for opt, arg in opts:
        if opt in ('-t', '--timeout'):
            timeout = int(arg)
        elif opt in ('-c', '--count'):
            count = int(arg)
        elif opt in ('-h', '--help'):
            print_help()
            sys.exit(0)
        else:
            assert False

    p1 = args[0]
    p2 = args[1]
    print_result(p1, p2, fight(p1, p2, count, timeout))
