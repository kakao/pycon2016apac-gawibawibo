import time


def __input(message):
    return input(message)

play = True
while play:
    player = __input('가위, 바위, 보!: ')
    player = player.lower()
    choice = ['가위', '바위', '보', 'rock', 'scissors', 'paper']
    while player not in choice:
        player = __input('가위, 바위, 보!: ')
        player = player.lower()

    # 0: 바위, 1: 보, 2: 가위
    if player in ['바위', 'rock']:
        player = 0
    elif player in ['보', 'paper']:
        player = 1
    else:
        player = 2

    millisecond = int(round(time.time() * 1000))
    computer = millisecond % 3

    # 결과출력
    if player == computer:
        print('비겼다')
    elif player == 0:
        if computer == 1:
            print('승리');
        if computer == 2:
            print('패배');
    elif player == 1:
        if computer == 0:
            print('승리');
        if computer == 2:
            print('패배');
    elif player == 2:
        if computer == 0:
            print('패배');
        if computer == 1:
            print('승리');
    finish = False
    while not finish:
        user_input = __input('계속하시겠습니까? Yes(y)/No(n): ')
        user_input = user_input.lower()
        if user_input in ['yes', 'y']:
            play = False
            finish = True
            print('종료')
        elif user_input in ['no', 'n']:
            finish = play = True

        else:
            finish = False
