import random

HAND = ['gawi', 'bawi', 'bo']

#�׳� ���� ������ ������������ ���Һ�
def show_me_the_hand(records):
    return HAND[random.randint(0,2)]

if __name__ == "__main__":
    print(show_me_the_hand([]))
