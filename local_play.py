import logging as L

_player_modules = {}


def get_player_module(player):
    try:
        return _player_modules[player.name]
    except KeyError:
        try:
            _player_modules[player.name] = __import__('player_' + player.name, globals(), locals(),
                                                      ['show_me_the_hand'])
            return _player_modules[player.name]
        except ImportError as e:
            L.error('error %r import module for player %s' % (e, player.name))
            return None  # 부전패!
        except Exception as e:
            L.error('unknown error %r import module for player %s' % (e, player.name))
            return None  # 부전패!
    except Exception as e:
        L.error('unknown error %r get module for player %s' % (e, player.name))
        return None  # 부전패!


def get_player_hand(player, records):
    try:
        hand = get_player_module(player).show_me_the_hand(records)
        if type(hand) is str:
            return hand
        L.error('unknown hand %s by player %s' % (hand, player.name))
        return None  # 부전패!
    except Exception as e:
        L.error('error %r while invoke show_me_the_hand function for player %s' % (e, player.name))
        return None  # 부전패!
