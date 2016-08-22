# 'gawi', 'bawi', 'bo'
def show_me_the_hand(records):
  if len(records) < 231:
    return 'bawi'
  elif len(records) < 312 :
    return 'gawi' if (len(records) % 2 == 0) else 'bo'
  else:
    if sum(x[0] == 'bawi' for x in records) / len(records) > 0.31 :
      return 'bo'
    else :
      return 'gawi'