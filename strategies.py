from copy import copy, deepcopy
import random
import math


"""

Classes to be used with tictactoe

"""


# Represents a strategy that one can perform in a game of ultimate tic tac toe
class RandomStrat(object):
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        if verbose:
            print('Making move randomly')
        # first check if you can move anywhere on the board, then randomly choose a board
        return make_move_random(game)

    def __str__(self):
        return 'Random'


# If the current board has the center open, don't move there. But we dooo want to play on the middle board if we are allowed to choose our boards
class NoCenterStrat():
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        if verbose:
            print('Not choosing middle if possible')
        # first check if you can choose the board to move to, if possible choose the middle board, since this strategy wants to win the middle board
        return make_move_center(game)

    def __str__(self):
        return 'No Center'


# search through the boards and
class WinAnyBoardStrat():
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        if verbose:
            print('We will try and win a board that we can win.')
        # first check if you can choose the board to move to, if possible choose the middle board, since this strategy wants to win the middle board
        result = win_any_board(game)
        if result is not None:
            return result
        # if we can't make a move randomly
        return make_move_random(game)

    def __str__(self):
        return 'Win Board'


# if your opponent is about to win, block them
class BlockOpponentStrat():
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        if verbose:
            print('We will try and block the opponents win.')
        # first try and block the opponent on a board they are about to win
        result = block_opponent(game)
        if result is not None:
            return result
        # if that doesnt work then simply choose randomly
        return make_move_random(game)

    def __str__(self):
        return 'Block'



# first try and win the current board, then try and block opponent
class WinThenBlockStrat():
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        if verbose:
            print('We will try and win the current board.')
        # first try and win the current game
        result = win_any_board(game)
        if result is not None:
            return result
        # second try and block the opponent on a board they are about to win
        result = block_opponent(game)
        if result is not None:
            return result
        # if neither of the above is satisfied then we move randomly
        return make_move_random(game)

    def __str__(self):
        return 'Win then Block'


# firs try and win the current board then move somewhere randomly that is not the center
class WinThenNoCenterStrat():
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        if verbose:
            print('Not choosing middle if possible')
        # first try and win the current board
        result = win_any_board(game)
        if result is not None:
            return result
        # then try and move to the center
        return make_move_center(game)

    def __str__(self):
        return 'Win then No Center'


# try and move only to center and corners on boards if possible
class NoCornersStrat():
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        if verbose:
            print('Not choosing middle if possible')
        # first try and win the current board
        result = take_middles_and_center(game)
        if result is not None:
            return result
        # then try and move to the center
        return make_move_random(game)

    def __str__(self):
        return 'No Corners'


# first try and win a board then focus on no corners
class WinThenNoCornersStrat():
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        if verbose:
            print('Not choosing middle if possible')
        # first try and win
        result = win_any_board(game)
        if result is not None:
            return result
        # first try and win the current board
        result = take_middles_and_center(game)
        if result is not None:
            return result
        # then try and move to the center
        return make_move_random(game)

    def __str__(self):
        return 'Win then No Corners'



"""
# try and win the current board in a more advanced way. This tries to first setup a 
class WinCurBoardAdvancedStrat():
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        if verbose:
            print('We will try and win the current board.')
        possible_moves = copy(game.get_current_board().get_open_spots())
        # first check to see if we can win the current board
        winnable_spots = copy(game.get_current_board().get_winnable_spots(game.get_current_player_turn()))
        for winnable in winnable_spots:
            if len(winnable) == 1:
                return winnable[0]
        # now check to see if there is a way to win in 2 moves, choose randomly between those 2 moves
        winnable_spots = copy(game.get_current_board().get_winnable_spots(game.get_current_player_turn()))
        for winnable in winnable_spots:
            if len(winnable) == 2:
                return winnable[round(random.random())]
        # if neither of these are true, move randomly
        assert len(possible_moves) != 0
        move_index = math.floor(len(possible_moves)*random.random())
        return possible_moves[move_index]

"""

"""

Classes used for checking board states in certain strategies

"""

# randomly choose a board and location on the board
def make_move_random(game):
    board = game.get_current_board_index()
    if game.move_anywhere:
        board_index = math.floor(len(game.get_open_boards())*random.random())
        board = game.get_open_boards()[board_index]
    possible_moves = game.get_board(board).get_open_spots()
    assert len(possible_moves) != 0 
    location = possible_moves[math.floor(len(possible_moves)*random.random())]
    return [location, board]


# if we can make a move to the center, then do it. Otherwise make a move 
def make_move_center(game):
    board = game.get_current_board_index()
    location = []
    # first check if you can choose the board to move to, if possible choose the middle board, since this strategy wants to win the middle board
    center = [1,1]
    if game.move_anywhere:
        openings = game.get_open_boards()
        if center in openings:
            board = center
        else:
            board = openings[ math.floor(len(openings) * random.random()) ]
    # now choose a move on that board
    possible_moves = copy(game.get_board(board).get_open_spots())
    if center in possible_moves and len(possible_moves) > 1:
        possible_moves.remove(center)
    assert len(possible_moves) != 0 
    location = possible_moves[math.floor(len(possible_moves)*random.random())]
    return [location, board]


# focus on taking the corners in boards
def take_middles_and_center(game):
    board = game.get_current_board_index()
    location = []
    # first check and see if we can move anywhere
    if game.move_anywhere:
        openings = game.get_open_boards()
        for open_board in openings:
            open_spots = game.get_board(open_board).get_open_spots()
            # the corners and the center all have number 1
            for spot in open_spots:
                if 1 in spot:
                    return [spot, open_board]
        board_index = math.floor(len(game.get_open_boards())*random.random())
        board = game.get_open_boards()[board_index]
    # now 
    open_spots = game.get_board(board).get_open_spots()
    # the corners and the center all have number 1
    for spot in open_spots:
        if 1 in spot:
            return [spot, board]
    return None


# try and win any board that we can
def win_any_board(game):
    board = game.get_current_board_index()
    location = None
    # first check if you can choose the board to move to, if possible choose the middle board, since this strategy wants to win the middle board
    if game.move_anywhere:
        openings = game.get_open_boards()
        for b in openings:
            winnable_spots = copy(game.get_board(b).get_winnable_spots(game.get_current_player_turn()))
            for winnable in winnable_spots:
                if len(winnable) == 1:
                    return [winnable[0], b]
        # if we do not find one we can win, then choose randomly
        board_index = math.floor(len(game.get_open_boards())*random.random())
        board = game.get_open_boards()[board_index]
    # now check and see if we can win the board we are placed on
    winnable_spots = copy(game.get_board(board).get_winnable_spots(game.get_current_player_turn()))
    for winnable in winnable_spots:
        if len(winnable) == 1:
            location = winnable[0]
    if location is None:
        return None
    return [location, board]


# if the opponent can win the current board then try and block them
def block_opponent(game):
    board = game.get_current_board_index()
    location = None
    # first check if we can move anywhere, in that case find a place to block an opponent
    if game.move_anywhere:
        openings = game.get_open_boards()
        for b in openings:
            opp_winnable_spots = copy(game.get_board(b).get_winnable_spots(game.get_other_player_turn()))
            for winnable in opp_winnable_spots:
                if len(winnable) == 1:
                    return [winnable[0], b]
        # if we don't find a place to block them, then just choose randomly
        board_index = math.floor(len(game.get_open_boards())*random.random())
        board = game.get_open_boards()[board_index]
    # check to see if the opponent can win the board we have chosen if so block them
    opp_winnable_spots = copy(game.get_board(board).get_winnable_spots(game.get_other_player_turn()))
    for winnable in opp_winnable_spots:
        if len(winnable) == 1:
            location = winnable[0]
    if location is None:
        return None
    return [location, board]

