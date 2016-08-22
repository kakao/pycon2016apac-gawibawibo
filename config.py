#!/usr/bin/env python3
# coding: utf-8
# vim: ts=4 sw=4 sts=4 expandtab

import os
import sys
import re

# 가위, 바위, 보
GAWI = 'gawi'  # u'\u270c'  #'gawi'
BAWI = 'bawi'  # u'\u270a'  #'bawi'
BO = 'bo'  # u'\u270b'  #'bo'

WIN_TABLE = {
    BAWI: GAWI,
    GAWI: BO,
    BO: BAWI,
}

VALID_HANDS = WIN_TABLE.keys()

# 승:3점, 무:1점, 패:0점
WIN_POINT = 3
TIE_POINT = 1
LOSE_POINT = 0

# SEASON = '0813'
SEASON = '0814'
# SEASON = 'test'
MATCH_COUNT_FULL_LEAGUE = 100
MATCH_COUNT_TOURNAMENT = 1000
MATCH_COUNT_SEMIFINAL = 5000
MATCH_COUNT_FINAL = 10000
PLAYER_TIMEOUT = 1000
# MAX_PLAYER = 100

_PLAYER_MODULE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), SEASON)
# XXX: player 모듈들 import 경로에 추가
# sys.path.append(_PLAYER_MODULE_DIR)
# 참가자 수 ::= 디렉토리의 _player_*.py 파일 갯수
PLAYERS = list(filter(lambda name: re.fullmatch(r'player_.+\.py', name), os.listdir(_PLAYER_MODULE_DIR)))
MAX_PLAYER = len(PLAYERS)


# print('***** prepare season %s with %d players in %s' % (SEASON, MAX_PLAYER, _PLAYER_MODULE_DIR))


def player_module_file(name):
    return os.path.join(_PLAYER_MODULE_DIR, 'player_%s.py' % name)


def compare_hands(h1, h2):
    if h1 == h2:
        return 0  # 무승부
    elif h1 in VALID_HANDS and (h2 is None or WIN_TABLE[h1] == h2):
        return 1  # h1 승
    elif h2 in VALID_HANDS and (h1 is None or WIN_TABLE[h2] == h1):
        return -1  # h2 승
    return 0  # ???


def get_score(win, tie, lose):
    return win * WIN_POINT + tie * TIE_POINT + lose * LOSE_POINT
