
from datetime import datetime

def show_me_the_hand(records):
 d = datetime.now()
 microsec = d.microsecond % 3
 result =""
 if microsec == 0:
  result = "bawi"
 elif microsec == 1:
  result = "bo"
 else:
  result = "gawi"

 return result