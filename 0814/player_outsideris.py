import time

def show_me_the_hand(records):
  rps = ['gawi', 'bawi', 'bo']

  gawiPercent = 0
  bawiPercent = 0 
  boPercent = 0 

  if (len(records) > 30):
    gawiPercent = [r for r, _ in records].count('gawi') / len(records) * 100
    bawiPercent = [r for r, _ in records].count('bawi') / len(records) * 100
    boPercent = [r for r, _ in records].count('bo') / len(records) * 100

    if (gawiPercent < 15 or bawiPercent < 15 or boPercent < 15):
      if (gawiPercent < 15): 
        rps.remove('bawi')
        rps.remove('gawi')
      if (bawiPercent < 15): 
        rps.remove('bo')
        rps.remove('bawi')
      if (boPercent < 15): 
        rps.remove('gawi')
        rps.remove('bo')
  else:
    rps = ['gawi', 'bawi']
  
  return rps[rand(len(rps))]

def rand(max):
  return int(time.time() % max)
