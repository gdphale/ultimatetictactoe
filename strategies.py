from copy import copy, deepcopy
import random
import math

# Represents a strategy that one can perform in a game of ultimate tic tac toe
class RandomStrat(object):
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        board = game.get_current_board_index()
        location = []
        if verbose:
            print('Making move randomly')
        # first check if you can move anywhere on the board, then randomly choose a board
        if game.move_anywhere:
            openings = game.get_open_boards()
            board = openings[ math.floor(len(openings) * random.random()) ]
        # then randomly choose a location on that board
        possible_moves = game.get_board(board).get_open_spots()
        assert len(possible_moves) != 0 
        location = possible_moves[math.floor(len(possible_moves)*random.random())]
        return [location, board]


# If the current board has the center open, don't move there. But we dooo want to play on the middle board if we are allowed to choose our boards
class NoCenterStrat():
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        board = game.get_current_board_index()
        location = []
        if verbose:
            print('Not choosing middle if possible')
        # first check if you can choose the board to move to, if possible choose the middle board, since this strategy wants to win the middle board
        center = [1,1]
        if game.move_anywhere:
            openings = game.get_open_boards()
            if center in openings:
                board = center
            else:
                board = openings[ math.floor(len(openings) * random.random()) ]
        # now choose a move on that board
        possible_moves = game.get_board(board).get_open_spots()
        if center in possible_moves and len(possible_moves) > 1:
            possible_moves.remove(center)
        assert len(possible_moves) != 0 
        location = possible_moves[math.floor(len(possible_moves)*random.random())]
        return [location, board]


# if you can win the current board, do it
class WinCurBoardStrat():
    """docstring for ClassName"""
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
        # if we can't win any, simply move randomly
        assert len(possible_moves) != 0
        move_index = math.floor(len(possible_moves)*random.random())
        return possible_moves[move_index]


# if your opponent is about to win, block them
class BlockOpponentStrat():
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        if verbose:
            print('We will try and block the opponents win.')
        possible_moves = copy(game.get_current_board().get_open_spots())
        # first check to see if the opponent can win the current board, if so block them
        opp_winnable_spots = copy(game.get_current_board().get_winnable_spots(game.get_other_player_turn()))
        for winnable in opp_winnable_spots:
            if len(winnable) == 1:
                return winnable[0]
        # if we can't win any, simply move randomly
        assert len(possible_moves) != 0
        move_index = math.floor(len(possible_moves)*random.random())
        return possible_moves[move_index]


# first try and win the current board, then try and block opponent
class WinThenBlockStrat():
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        if verbose:
            print('We will try and win the current board.')
        possible_moves = copy(game.get_current_board().get_open_spots())
        # first try and win the current board
        winnable_spots = copy(game.get_current_board().get_winnable_spots(game.get_current_player_turn()))
        for winnable in winnable_spots:
            if len(winnable) == 1:
                return winnable[0]
        # then check to see if the opponent can win the current board, if so block them
        opp_winnable_spots = copy(game.get_current_board().get_winnable_spots(game.get_other_player_turn()))
        for winnable in opp_winnable_spots:
            if len(winnable) == 1:
                return winnable[0]
        # if we can't win any, simply move randomly
        assert len(possible_moves) != 0
        move_index = math.floor(len(possible_moves)*random.random())
        return possible_moves[move_index]


# firs try and win the current board then move somewhere randomly that is not the center
class WinThenNoCenterStrat():
    """docstring for ClassName"""
    def __init__(self):
        return None
    
    def decide_move(self, game, verbose = False):
        if verbose:
            print('Not choosing middle if possible')
        # first try and win the current board
        winnable_spots = copy(game.get_current_board().get_winnable_spots(game.get_current_player_turn()))
        for winnable in winnable_spots:
            if len(winnable) == 1:
                return winnable[0]
        # if we can't win then try and not go to the center
        center = [1,1]
        possible_moves = copy(game.get_current_board().get_open_spots())
        if center in possible_moves and len(possible_moves) > 1:
            possible_moves.remove(center)
        assert len(possible_moves) != 0 
        move_index = math.floor(len(possible_moves)*random.random())
        return possible_moves[move_index]


# try and win the current board in a more advanced way. This tries to first setup a 
class WinCurBoardAdvancedStrat():
    """docstring for ClassName"""
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


# first trt and win, then try and block then go for the corners








