def show_me_the_hand(records):
  """
  Input
  =====
    records: a list like [(gawi/bawi/bo, 1(=승리)/0/-1), ...]
  """
  import time
  initial_set = ['gawi', 'bawi', 'bo']
  if len(records) == 0:
    pass
  else:
    for record, score in records:
      #if score == -1 or 0:
      #  continue
      if record == "gawi":
        initial_set.append('bawi')
      elif record == "bawi":
        initial_set.append('bo')
      else: #record == "bo:
        initial_set.append('gawi')
  rand = int(time.time() % len(initial_set))

  return initial_set[rand]