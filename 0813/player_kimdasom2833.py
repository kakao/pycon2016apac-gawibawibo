import random

HAND = ['gawi', 'bawi', 'bo']

#그냥 랜덤 어차피 가위바위보는 복불복
def show_me_the_hand(records):
    return HAND[random.randint(0,2)]

if __name__ == "__main__":
    print(show_me_the_hand([]))
