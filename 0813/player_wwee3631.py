from random import choice
from random import random

next = {}
next['gawi'] = 'bo'
next['bawi'] = 'gawi'
next['bo'] = 'bawi'


def show_me_the_hand(records):
  # 최초 한번은 랜덤...
  if len(records) == 0:
      return choice(['gawi', 'bawi', 'bo'])
  # 이후에는 상대방이 낸 걸 따라내는 플레이어
  if random() < 0.1:
        return choice(['gawi', 'bawi', 'bo'])
  return next[records[0][0]]


