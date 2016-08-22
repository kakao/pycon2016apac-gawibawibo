#!/usr/bin/env python3
# coding: utf-8
# vim: ts=4 sw=4 sts=4 expandtab
import os
import re
import sys
import logging as L

from flask import Flask, request, redirect, render_template, jsonify

from db import db
from game import *
from handbattle import fight

from config import *

app = Flask(__name__)

# app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/' + SEASON + '.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)
db.create_all()


@app.route('/', methods=['GET'])
def index():
    players = get_players(MAX_PLAYER)
    round32 = get_games_round_of(32)
    round16 = get_games_round_of(16)
    round8 = get_games_round_of(8)
    semifinal = get_games_round_of(4)
    finals = get_games_round_of(2)
    final = finals[0] if len(finals) > 0 else None
    winners = get_winners(2)
    winner = winners[0] if len(winners) > 0 else None
    return render_template('index.html',
                           max_player=MAX_PLAYER,
                           match_count_full_league=MATCH_COUNT_FULL_LEAGUE,
                           match_count_tournament=MATCH_COUNT_TOURNAMENT,
                           match_count_semifinal=MATCH_COUNT_SEMIFINAL,
                           match_count_final=MATCH_COUNT_FINAL,
                           players=players,
                           round32=round32,
                           round16=round16,
                           round8=round8,
                           semifinal=semifinal,
                           final=final,
                           winner=winner)


@app.route('/prepare_full_league_games')
def do_prepare_full_league_games():
    prepare_full_league_games(MAX_PLAYER)
    return redirect('/')


@app.route('/play_games')
def do_play_games():
    round_of = int(request.args.get('round_of'))
    match_count = int(request.args.get('match_count'))
    play_games(round_of, match_count)
    return redirect('/')


@app.route('/prepare_tournament_games')
def do_prepare_tournament_games():
    round_of = int(request.args.get('round_of'))
    prepare_tournament_games(round_of)
    return redirect('/')


@app.route('/test')
def test():
    return render_template('test.html',
                           max_player=MAX_PLAYER,
                           match_count_full_league=MATCH_COUNT_FULL_LEAGUE,
                           match_count_tournament=MATCH_COUNT_TOURNAMENT,
                           match_count_semifinal=MATCH_COUNT_SEMIFINAL,
                           match_count_final=MATCH_COUNT_FINAL)


@app.route('/reset_db')
def do_reset_db():
    reset_db()
    return redirect('/test')


@app.route('/create_test_players')
def do_create_test_players():
    max_player = int(request.args.get('max_player'))
    create_test_players(max_player)
    return redirect('/test')


@app.route('/play_test_games')
def do_play_test_games():
    max_player = int(request.args.get('max_player'))
    tournament_round = int(request.args.get('tournament_round'))
    match_count = int(request.args.get('match_count'))
    play_test_games(max_player, tournament_round, match_count)
    return redirect('/test')


@app.route('/play_test_game')
def do_play_test_game():
    p1 = player_module_file(request.args.get('p1'))
    p2 = player_module_file(request.args.get('p2'))
    try:
        count = int(request.args.get('count'))
    except:
        count = MATCH_COUNT_FULL_LEAGUE
    try:
        timeout = int(request.args.get('timeout'))
    except:
        timeout = PLAYER_TIMEOUT
    return jsonify(fight(p1, p2, count, timeout))


if __name__ == '__main__':
    L.basicConfig(level=L.INFO)
    app.run()
