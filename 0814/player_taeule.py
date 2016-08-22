

def show_me_the_hand(records):
  result = 'bo'

  # 최초 한 번은 무조건 보
  if len(records) == 0:
    return result

  frequent = {'gawi': 0, 'bawi': 0, 'bo': 0}

  for idx, tuple in enumerate(records):

    (key, rs) = tuple

    val = frequent[key] + 1
    frequent[key] = val

  highKey = 'gawi'
  highFrequent = frequent[highKey]
  for k in frequent:
    val = frequent[k]

    if highFrequent < val:
      highKey = k
      highFrequent = val

  if highKey == 'gawi':
    result = 'bawi'

  elif highKey == 'bawi':
    result = 'bo'

  elif highKey == 'bo':
    result = 'gawi'

  else:
    result = 'bo'

  print(result)

  return result


