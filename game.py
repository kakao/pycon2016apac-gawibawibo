#!/usr/bin/env python3
# coding: utf-8
# vim: ts=4 sw=4 sts=4 expandtab
import logging as L
from sqlalchemy import text, desc
from random import choice
from time import sleep
from db import db, Player, Game, Match
from config import *
from handbattle import PlayerStub


def get_players(max_player):
    # return Player.query.order_by(desc(Player.at)).limit(max_player).all()
    return Player.query.order_by(desc(Player.total_score)).limit(max_player).all()


def get_player(name):
    return Player.query.get(name)


def get_player_games(name):
    return Game.query.filter((Match.p1 == name) | (Match.p2 == name)).all()


def get_games():
    return Game.query.all()


def get_game(id):
    return Game.query.get(id)


def get_game_matches(id):
    return Game.query.get(id).matches.all()


def get_matches():
    return Match.query.all()


def get_match(id):
    return Match.query.get(id)


def get_games_round_of(round_of):
    return Game.query.filter(Game.round_of == round_of) \
        .order_by(desc(Game.score)) \
        .order_by(desc(Game.delta)) \
        .all()


def get_winners(round_of):
    games = Game.query.filter(Game.round_of == round_of).all()
    winners = []
    for g in games:
        winners.append(Player.query.get(g.winner))
    return winners


def clear_games(round_of):
    db.session.query(Game).filter(Game.round_of == round_of).delete()
    db.session.query(Match).filter(Match.round_of == round_of).delete()
    db.session.commit()


def get_play_records(p):
    # FIXME: ....
    records = []
    rows = db.engine.execute(text(
        'SELECT h1,h2,at FROM match WHERE p1="%s" UNION SELECT h2,h1,at FROM match WHERE p2="%s" ORDER BY at DESC'
        % (p.name, p.name)))
    # 최근 경기부터... 시간 역순
    for row in rows:
        records.append((row[0], compare_hands(row[0], row[1])))
    # L.debug('records %r' % records)
    return records


def prepare_full_league_games(max_player):
    L.info('***** prepare full league games for %d players' % max_player)
    players = get_players(max_player)
    for p1 in players:
        for p2 in players:
            if p1.name == p2.name:
                break
            g = Game(p1.name, p2.name, 0)
            db.session.add(g)
            db.session.commit()
            L.info('prepare game#%d full league %s vs %s' % (g.id, p1.name, p2.name))


def prepare_tournament_games(round_of):
    L.info('***** prepare tournament games for round of %d' % round_of)
    # 직전 라운드(16강)는 이번 라운드(8강) * 2
    # 직전 라운드(16강) 결과에서 이번 라운드(8강) 대진표가 정해짐
    games = get_games_round_of(round_of * 2)
    # 토너먼트: 직전 라운드의 경기 수 == 이번 라운드 번호
    if len(games) == round_of:
        # 이번 라운드 경기수 = 이번 라운드(8강) / 2
        for i in range(int(round_of / 2)):
            # 앞쪽 반을 순회하면서.. 뒤쪽 반은 역순으로...
            # 최고점자 vs 최저점자
            p1 = games[i].winner
            p2 = games[- 1 - i].winner
            g = Game(p1, p2, round_of)
            db.session.add(g)
            db.session.commit()
            L.info('prepare game#%d round of #%d : %s vs %s' % (g.id, round_of, p1, p2))
    # 예선 풀 리그: 직전 라운드의 경기 수 == 0
    else:
        # FIXME: ....
        players = get_players(round_of)
        # 이번 라운드 경기수 = 이번 라운드(8강) / 2
        for i in range(int(round_of / 2)):
            # 앞쪽 반을 순회하면서.. 뒤쪽 반은 역순으로...
            # 최고점자 vs 최저점자
            p1 = players[i].name
            p2 = players[- 1 - i].name
            g = Game(p1, p2, round_of)
            db.session.add(g)
            db.session.commit()
            L.info('prepare game#%d round of #%d : %s vs %s' % (g.id, round_of, p1, p2))


def play_games(round_of, match_count):
    games = get_games_round_of(round_of)
    L.info('%d games', len(games))
    for g in games:
        L.info('play game#%d round of #%d : %s vs %s' % (g.id, g.round_of, g.p1, g.p2))
        showdown(g, match_count)


def showdown(g, match_count):
    p1 = get_player(g.p1)
    p2 = get_player(g.p2)
    p1_win = 0
    p2_win = 0
    tie = 0
    p1_records = get_play_records(p1)
    p2_records = get_play_records(p2)

    #
    # using ganadist's handbattle module
    #
    p1_error = False
    p2_error = False

    try:
        player1 = PlayerStub(player_module_file(p1.name), PLAYER_TIMEOUT, p1_records)
    except Exception as e:
        L.error('player %s create error:' % p1.name, e)
        p1_error = True
    try:
        player2 = PlayerStub(player_module_file(p2.name), PLAYER_TIMEOUT, p2_records)
    except Exception as e:
        L.error('player %s create error:' % p2.name, e)
        p2_error = True

    if not p1_error and not p2_error:
        sleep(.05)
        for i in range(match_count):
            try:
                h1 = player1.get_hand()
            except Exception as e:
                L.error('player %s get hand error: %r' % (p1.name, e))
                p1_error = True
            try:
                h2 = player2.get_hand()
            except Exception as e:
                L.error('player %s get hand error: %r' % (p2.name, e))
                p2_error = True

            # if p1_error or p2_error:
            #     break

            hc = compare_hands(h1, h2)
            if hc > 0:
                p1_win += 1
                p1_point = WIN_POINT
                p2_point = LOSE_POINT
            elif hc < 0:
                p2_win += 1
                p1_point = LOSE_POINT
                p2_point = WIN_POINT
            else:
                tie += 1
                p1_point = TIE_POINT
                p2_point = TIE_POINT

            try:
                player1.send_result(h2, -hc)
            except Exception as e:
                L.error('player %s send_result error: %r' % (p1.name, e))
                p1_error = True
            try:
                player2.send_result(h1, hc)
            except Exception as e:
                L.error('player %s send_result error: %r' % (p2.name, e))
                p2_error = True

            # if p1_error or p2_error:
            #     break

            L.info('match#%d - %s(%s %d) vs %s(%s %d)' % (i, p1.name, h1, p1_point, p2.name, h2, p2_point))
            m = Match(g.id, g.round_of, p1.name, p2.name, str(h1), str(h2), p1_point, p2_point)
            db.session.add(m)
        # safe-guard
        sleep(.05)
        player1.stop()
        player2.stop()

    #
    # using iolo's local play
    #
    # p1_module = get_player_module(p1)
    # p2_module = get_player_module(p2)
    # if (not p1_module) and (not p2_module):
    #     L.info('**** both not ready --> all tie w/o matches')
    #     tie = match_count
    # elif p1_module and (not p2_module):
    #     L.info('**** p1 ready only --> p1 win w/o matches')
    #     p1_win = match_count
    # elif p2_module and (not p1_module):
    #     L.info('**** p2 ready only --> p2 win w/o matches')
    #     p2_win = match_count
    # else:
    #     p1_records = get_play_records(p1)
    #     p2_records = get_play_records(p2)
    #     L.debug('**** both ready --> total %d matches for round of %d' % (match_count, g.round_of))
    #     for cur_match in range(match_count):
    #         h1 = get_player_hand(p1, p2_records)
    #         h2 = get_player_hand(p2, p1_records)
    #         hc = compare_hands(h1, h2)
    #         if hc > 0:
    #             p1_win += 1
    #             p1_point = WIN_POINT
    #             p2_point = LOSE_POINT
    #         elif hc < 0:
    #             p2_win += 1
    #             p1_point = LOSE_POINT
    #             p2_point = WIN_POINT
    #         else:
    #             tie += 1
    #             p1_point = TIE_POINT
    #             p2_point = TIE_POINT
    #         L.debug('match#%d - %s(%s %d) vs %s(%s %d)' % (cur_match, p1.name, h1, p1_point, p2.name, h2, p2_point))
    #         m = Match(g.id, g.round_of, p1.name, p2.name, str(h1), str(h2), p1_point, p2_point)
    #         db.session.add(m)
    #         # 최근 경기부터... 시간 역순
    #         p1_records.insert(0, (h1, hc))
    #         p2_records.insert(0, (h2, -hc))

    # 플레이어 모듈에서 에러가 발생하면.. 몰수승 or 몰수패
    if p1_error and p2_error:
        L.info('**** both players error:  tie all w/o match')
        tie = match_count
    elif p1_error:
        L.info('**** only player %s error: lose all w/o match' % p1.name)
        p2_win = match_count
    elif p2_error:
        L.info('**** only player %s error: lose all w/o match' % p2.name)
        p1_win = match_count

    # 게임 점수 = 매치 점수 합계
    g.p1_win = p1_win
    g.p2_win = p2_win
    g.tie = tie
    g.p1_score = get_score(p1_win, tie, p2_win)
    g.p2_score = get_score(p2_win, tie, p1_win)
    # 승점...
    L.info('game#%d winner by score : %s(%d) vs %s(%d)' % (g.id, p1.name, g.p1_score, p2.name, g.p2_score))
    if g.p1_score > g.p2_score:
        g.winner = p1.name
    elif g.p1_score < g.p2_score:
        g.winner = p2.name
    else:
        # 동점이면 다승...
        L.info('***TIE*** game#%d winner by win : %s(%d) vs %s(%d)' % (g.id, p1.name, p1_win, p2.name, p2_win))
        if p1_win > p2_win:
            g.winner = p1.name
        elif p1_win < p2_win:
            g.winner = p2.name
        else:
            # 승수도 같으면... 등록시간!
            L.info('***MORE TIE*** game#%d winner by at : %s(%r) vs %s(%r)' % (g.id, p1.name, p1.at, p2.name, p2.at))
            if p1.at < p2.at:
                g.winner = p1.name
            elif p1.at > p2.at:
                g.winner = p2.name
            else:
                # 그마저도 같으면..??? 그냥 랜덤!
                L.info('***MOST TIE*** game#%d winner by random : %s vs %s' % (g.id, p1.name, p2.name))
                g.winner = choice([p1.name, p2.name])
    g.score = max(g.p1_score, g.p2_score)
    g.delta = abs(g.p1_score - g.p2_score)
    # 플레이어 통산 전적
    p1.win += p1_win
    p1.tie += tie
    p1.lose += p2_win
    p2.win += p2_win
    p2.tie += tie
    p2.lose += p1_win
    db.session.commit()


def reset_db():
    db.create_all()
    db.session.query(Player).delete()
    db.session.query(Game).delete()
    db.session.query(Match).delete()
    db.session.commit()


def create_test_players(max_player):
    for i in range(max_player):
        db.session.add(Player('p%d' % i, 'test%d' % i))
    db.session.commit()


def play_test_games(max_player, tournament_round, match_count):
    prepare_full_league_games(max_player)
    play_games(0, match_count)
    L.info('>>>>> promote to tournament: %r' % get_winners(0)[:tournament_round])
    round_of = tournament_round
    while round_of > 8:
        prepare_tournament_games(round_of)
        play_games(round_of, match_count)
        L.info('>>>>> promote to round of %d' % int(round_of / 2), get_winners(round_of))
        round_of = int(round_of / 2)
    prepare_tournament_games(8)
    play_games(8, match_count)
    L.info('>>>>> promote to semi-final: %r' % get_winners(8))
    prepare_tournament_games(4)
    play_games(4, match_count)
    L.info('>>>>> promote to final: %r' % get_winners(4))
    prepare_tournament_games(2)
    play_games(2, match_count)
    L.info('>>>>> final winner: %r' % get_winners(2))
