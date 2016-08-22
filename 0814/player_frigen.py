from collections import Counter
from functools import partial
import code # For debugging
import inspect

DEBUG = False

def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def get_most_common_result(f, n):
    # Run function `n` times and returns the most common result
    counter = Counter(f() for _ in range(n))
    return counter.most_common(1)[0][0]

IAMSPECIAL = True # Identifier for myself
ITERATION = 10 # How many iteration to test opponent move

ROCK = 'bawi'
PAPER = 'bo'
SCISSOR = 'gawi'

win_dict = {
    ROCK: PAPER,
    PAPER: SCISSOR,
    SCISSOR: ROCK
}

lose_dict = {
    PAPER: ROCK,
    SCISSOR: PAPER,
    ROCK: SCISSOR
}

def show_me_the_hand(records):
    try: # Wrap all in case everything goes wrong
        current_frame = inspect.currentframe()
        called_frame_info = inspect.getouterframes(current_frame, 2)
        called_frame = called_frame_info[-1][0]
        players = [obj for key, obj in called_frame.f_locals.items() if getattr(obj, 'show_me_the_hand', False)]
        player_functions = [player.show_me_the_hand for player in players if not getattr(player, 'IAMSPECIAL', False)] # Exclude myself

        if len(player_functions) == 1:
            # Yay it found the opponent!
            try:
                opponent_function = player_functions[0]
                return counter_opponent(opponent_function, records)
            except Exception:
                debug('exception1')
                pass
        elif len(player_functions) > 1:
            # Oh no, there's more than one opponent!
            # Assume the most referenced (in the frame) is the opponent
            counter = Counter(player_functions)
            opponent_function = counter.most_common(1)[0][0]
            try:
                return counter_opponent(opponent_function, records)
            except Exception:
                debug('exception2')
                pass
        else:
            debug('opponent not found!')
    except Exception:
        pass
    #code.interact(local=locals())

    # Fallback to simple PRNG
    return [ROCK, PAPER, SCISSOR][prng(len(records)) % 3] 


def counter_opponent(opponent_function, records):
    try:
        opponent_records = get_opponent_records(records)
        guessed_move = get_most_common_result(partial(opponent_function, opponent_records), ITERATION)
        return win_dict[guessed_move]
    except Exception:
        debug('exception occured!')
        raise


def get_opponent_records(my_records):
    """ Reconstruct opponent's record with my record """
    opponent_records = []
    for move, win in my_records:
        if win == 0: # tie
            opponent_records.append((move, -win))
        elif win < 0:
            opponent_records.append((win_dict[move], -win))
        elif win > 0:
            opponent_records.append((lose_dict[move], -win))
    return opponent_records

def prng(n):
    x = 111131111
    a = 123456789
    b = 1
    p = 99999199999 # Yes, it's a prime
    for _ in range(n):
        x = (a * x + b) % p 
    return x
