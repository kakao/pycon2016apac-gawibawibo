# coding:UTF-8
import random
code = ('Rock', 'Paper', 'Scisslor')
_win = 0
_lose = 0
_user_r = ""
_com_r = ""

def RPS_User():
 print"가위바위보"
 print "가위 : 1, 보 : 2, 바위 : 3 : "
 _user = input()
 if _user == 1:
  _user_r = code[2]
 elif _user == 2:
  _user_r = code[1]
 elif _user == 3:
  _user_r = code[0]
 else:
  print("꺼져")
 return _user_r
def RPS_Computer():
 comp = random.randint(1,3)
 if comp == 1:
  _com_r = code[2]
 elif comp == 2:
  _com_r = code[1]
 elif comp == 3:
  _com_r = code[0]
 return _com_r
def RPS_def(_user_r, _com_r):
 if _user_r == _com_r:
  print("비김")
 elif _user_r != _com_r:
  if _user_r == code[0]:
   if _com_r == code[1]:
    print("사용자 패배")
    _lose+1
   elif _com_r == code[2]:
    print("사용자 승리")
    _win+1
  elif _user_r == code[2]:
   if _com_r == code[1]:
    print("사용자 패배")
    _lose+1
   elif _com_r == code[0]:
    print("사용자 승리")
    _win+1
  elif _user_r == code[1]:
   if _com_r == code[0]:
    print("사용자 패배")
    _lose+1
   elif _com_r == code[1]:
    print("사용자 승리")
    _win+1
def RPS_run():
 a = RPS_User()
 b = RPS_Computer()
 RPS_def(a, b)
if __name__ == "__main__":
 a = RPS_run()
 print a


