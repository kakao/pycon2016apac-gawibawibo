#!/usr/bin/env python3
# coding: utf-8
# vim: ts=4 sw=4 sts=4 expandtab
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

db = SQLAlchemy()


class Player(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    endpoint = db.Column(db.String(80))
    win = db.Column(db.Integer)
    lose = db.Column(db.Integer)
    tie = db.Column(db.Integer)
    at = db.Column(db.DateTime)

    @hybrid_property
    def total_score(self):
        return self.win * 3 - self.tie * 1

    def __init__(self, name, endpoint, win=0, lose=0, tie=0, at=None):
        self.name = name
        self.endpoint = endpoint
        self.win = win
        self.lose = lose
        self.tie = tie
        if at is None:
            at = datetime.utcnow()
        self.at = at

    def __repr__(self):
        return '<Player %r>' % self.name


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    p1 = db.Column(db.String(80))
    p2 = db.Column(db.String(80))
    round_of = db.Column(db.Integer)  # 0=풀리그, 64=64강, 32=32강, 16=16강, 8=8강, 4=4강, 2=결승
    winner = db.Column(db.String(80))  # 승점 >> 다승 >> 등록시간
    score = db.Column(db.Integer)  # 승점 == max(p1_score, p2_score)
    delta = db.Column(db.Integer)  # 점수차 (승자 점수 - 패자 점수) == abs(p1_score - p2_score)
    p1_score = db.Column(db.Integer)  # p1_win * 3 + tie * 1 == select sum(p1_point) from match where game_id=:id
    p2_score = db.Column(db.Integer)  # p2_win * 3 + tie * 1 == select sum(p2_point) from match where game_id=:id
    p1_win = db.Column(db.Integer)
    p2_win = db.Column(db.Integer)
    tie = db.Column(db.Integer)
    at = db.Column(db.DateTime)

    def __init__(self, p1, p2, round_of=0, winner='', score=0, delta=0, p1_win=0, p2_win=0, tie=0, at=None):
        self.p1 = p1
        self.p2 = p2
        self.round_of = round_of
        self.winner = winner
        self.score = score
        self.delta = delta
        self.p1_win = p1_win
        self.p2_win = p2_win
        self.tie = tie
        if at is None:
            at = datetime.utcnow()
        self.at = at

    def __repr__(self):
        return '<Game %r>' % self.id


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer)
    round_of = db.Column(db.Integer)  # for easy query
    p1 = db.Column(db.String(80))  # for easy query
    p2 = db.Column(db.String(80))  # for easy query
    h1 = db.Column(db.String(80))  # enum GAWI, BAWI, BO
    h2 = db.Column(db.String(80))  # enum  GAWI, BAWI, BO
    p1_point = db.Column(db.Integer)  # win=3, tie=1, lose=0
    p2_point = db.Column(db.Integer)  # win=3, tie=1, lose=0
    at = db.Column(db.DateTime)

    def __init__(self, game_id, round_of, p1, p2, h1, h2, p1_point=0, p2_point=0, at=None):
        self.game_id = game_id
        self.round_of = round_of
        self.p1 = p1
        self.p2 = p2
        self.h1 = h1
        self.h1 = h1
        self.h2 = h2
        self.p1_point = p1_point
        self.p2_point = p2_point
        if at is None:
            at = datetime.utcnow()
        self.at = at

    def __repr__(self):
        return '<Match %r>' % self.id
