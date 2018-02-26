from copy import copy, deepcopy
import random
import math

"""
Board is a 3x3 grid of 3x3 grids.

board_single = [[0,0,0],
                [0,0,0],
                [0,0,0]]


board = [[deepcopy(board_single), deepcopy(board_single), deepcopy(board_single)],
         [deepcopy(board_single), deepcopy(board_single), deepcopy(board_single)],
         [deepcopy(board_single), deepcopy(board_single), deepcopy(board_single)]]

So examining the above board:
    - board[0][0] is the top left board
    - board[0][1] is the middle top board
    - board[0][2] is the top right board
    - board[2][0] is the bottom left board
    Each of these return a 3x3 grid with 
        - grid[0][1] is the top middle element

    So overall it is:
        board[vertical_board][horizontal_board][board_y-axis][board_x-axis]

"""

# creates an instance of an ultimate tic-tac-toe game
# represents the game state as a 2-d array of 2-d arrays.
# has certain aspects to the game state:
#   - current board state
#   - current player's turn
# '| - - - | - - - | - - - |'


# Represents one board of Tic Tac Toe. Stores certain metrics on the board state
class Board(object):
    """ A standard 3x3 tictactoe board """
    def __init__(self):
        self.board = [[2,2,2],
                      [2,2,2],
                      [2,2,2]]
        self.__init_spots()
        self.__init_winnable_states()
        self.winner = None

    # Initialize the board object storing the moves each player has made on the board
    def __init_spots(self):
        # initialize the open spots for the entire board
        self.open_spots = []
        for i in range(3):
            for j in range(3):
                self.open_spots.append([i,j])
        # taken spots by player 1 and player 2
        self.p0_spots = []
        self.p1_spots = []

    # creates the winnable states for both players
    def __init_winnable_states(self):
        self.p0_winnable_states = self.__create_all_states()
        self.p1_winnable_states = self.__create_all_states()

    # returns the winnable states for a person playing
    def __create_all_states(self):
        states = []
        for vert in range(3):
            winnable = []
            for hor in range(3):
                winnable.append([vert, hor])
            states.append(winnable)
        for hor in range(3):
            winnable = []
            for vert in range(3):
                winnable.append([vert, hor])
            states.append(winnable)
        winnable = []
        for i in range(3):
            winnable.append([i,i])
        states.append(winnable)
        winnable = []
        for i in range(3):
            winnable.append([2 - i, i])
        states.append(winnable)
        return states

    # updates the winnable states after someone makes a move
    def __update_winnable_states(self, location, player):
        if player == 0:
            for state in self.p0_winnable_states:
                if location in state:
                    state.remove(location)
                if len(state) == 0 and self.winner is None:
                    self.winner = 0
            to_remove = []
            for state in self.p1_winnable_states:
                if location in state:
                    to_remove.append(state)
            for item in to_remove:
                self.p1_winnable_states.remove(item)
        if player == 1:
            for state in self.p1_winnable_states:
                if location in state:
                    state.remove(location)
                if len(state) == 0 and self.winner is None:
                    self.winner = 1
            to_remove = []
            for state in self.p0_winnable_states:
                if location in state:
                    to_remove.append(state)
            for item in to_remove:
                self.p0_winnable_states.remove(item)

    # get the winnable spots on this board for the given player
    def get_winnable_spots(self, player):
        if player == 0:
            return self.p0_winnable_states
        elif player == 1:
            return self.p1_winnable_states
        # should never hit here
        return None

    # Mark an open spot 
    def make_move(self, location, player):
        assert location in self.open_spots
        self.board[location[0]][location[1]] = player
        self.open_spots.remove(location)
        if player == 0:
            self.p0_spots.append(location)
        elif player == 1:
            self.p1_spots.append(location)
        self.__update_winnable_states(location, player)

    # returns an array of arrays, which are the opening [vertical, horizontal] spots available on this board
    def get_open_spots(self):
        return self.open_spots

    # returns the value being stored in the current location of the Board.
    # 0 = player 0 claimed it, 1 = player 1 claimed it, 2 = unclaimed
    def get_value(self, location):
        return self.board[location[0]][location[1]]

    def get_winner(self):
        return self.winner



# Defines a game of Ultimate Tic Tac Toe
class Game(object):
    """initializes a new game"""
    def __init__(self, strat0 = None, strat1 = None, goes_first=None):
        # initialize the open spots for the board
        self.open_boards = []
        for i in range(3):
            for j in range(3):
                self.open_boards.append([i,j])
        self.strat0 = strat0
        self.strat1 = strat1
        if goes_first is None:
            self.players_turn = round(random.random())
        else:
            self.players_turn = goes_first
        self.playing_board = [math.floor(3*random.random()), math.floor(3*random.random())]
        self.__init_board()
        self.__init_winnable_states()
        self.winner = None
        self.move_anywhere = False

    # initializes a new game board
    def __init_board(self):
        self.board = [[Board(), Board(), Board()],
                      [Board(), Board(), Board()],
                      [Board(), Board(), Board()]]

    # used for printing game state
    def __print_game_line(self):
        print('|  -    -    -  |  -    -    -  |  -    -    -  |')

    # returns the character that corresponds to the value stored in the game board array
    def __get_character(self, value):
        if value == 2:
            return 'N'
        elif value == 1:
            return 'X'
        elif value == 0:
            return 'O'

    # initialize the winnable states for the larger board
    def __init_winnable_states(self):
        self.p0_winnable_states = self.__create_all_states()
        self.p1_winnable_states = self.__create_all_states()

    # create the winnable states for the larger board
    def __create_all_states(self):
        states = []
        for vert in range(3):
            winnable = []
            for hor in range(3):
                winnable.append([vert, hor])
            states.append(winnable)
        for hor in range(3):
            winnable = []
            for vert in range(3):
                winnable.append([vert, hor])
            states.append(winnable)
        winnable = []
        for i in range(3):
            winnable.append([i,i])
        states.append(winnable)
        winnable = []
        for i in range(3):
            winnable.append([2 - i, i])
        states.append(winnable)
        return states

    # updates the winnable states after someone makes a move
    def __update_winnable_states(self, location, player):
        if player == 0:
            to_remove = []
            # go through the possible ways to win and get rid of those options that use the 
            # move that was just made
            for state in self.p0_winnable_states:
                if location in state:
                    state.remove(location)
                if len(state) == 0 and self.winner is None:
                    self.winner = 0
            to_remove = []
            for state in self.p1_winnable_states:
                if location in state:
                    to_remove.append(state)
            for item in to_remove:
                self.p1_winnable_states.remove(item)
        if player == 1:
            for state in self.p1_winnable_states:
                if location in state:
                    state.remove(location)
                if len(state) == 0 and self.winner is None:
                    self.winner = 1
            to_remove = []
            for state in self.p0_winnable_states:
                if location in state:
                    to_remove.append(state)
            for item in to_remove:
                self.p0_winnable_states.remove(item)

    # get who's turn it is, player 0 or 1
    def get_current_player_turn(self):
        return self.players_turn

    # get the player who currently isn't playing
    def get_other_player_turn(self):
        return abs(self.get_current_player_turn() - 1)

    # prints out the current game state
    def print_board(self):
        for vertical_board in range(3):
            self.__print_game_line()
            for vertical_index in range(3):
                for horizontal_board in range(3):
                    print('|', end='')
                    for horizontal_index in range(3):
                        print(' ', self.__get_character(self.board[vertical_board][horizontal_board].get_value([vertical_index, horizontal_index])), ' ', end='')
                print('|')
        self.__print_game_line()

    # returns the current Board being played on
    def get_current_board(self):
        if self.move_anywhere:
            return None
        return self.board[self.playing_board[0]][self.playing_board[1]]

    # return the board at the given location
    def get_board(self, location):
        return self.board[location[0]][location[1]]

    # returns the index of the Board being played on
    def get_current_board_index(self):
        return self.playing_board

    # print the current Board being played on
    def print_current_board(self):
        current_board = self.get_current_board()
        print('|  -    -    -  |')
        for vertical in range(3):
            print('|', end='')
            for horizontal in range(3):
                print(' ', self.__get_character(current_board.get_value([vertical, horizontal])), ' ', end='')
            print('|')
        print('|  -    -    -  |')

    # make a move as the current player
    def make_move(self, location, board, verbose = False):
        # ensure the correct decision was made
        if not self.move_anywhere:
            assert board == self.playing_board
        # ensure that the move can be made
        assert location in self.get_board(board).get_open_spots()
        old_val = self.winner
        # print the state of the game after the move
        if verbose:
            print('My current board is: ', self.get_current_board_index())
            print('I am making a move on index: ', location, ' and on the board: ', board)
        # make the move that the player specified
        self.get_board(board).make_move(location, self.players_turn)
        if self.get_board(board).get_winner() is not None:
            self.__update_winnable_states(board, self.players_turn)
        # remove if the board was tied or won
        if len(self.get_board(board).open_spots) == 0 or self.get_board(board).get_winner() is not None:
            self.open_boards.remove(board)
        # check if the game was a tie
        if len(self.open_boards) == 0 and self.winner is None:
            if verbose:
                print('The game was a tie.')
            return 3
        # check if someone has won the game
        if self.winner is not None:
            if verbose:
                print('Player ', str(self.winner), ' won the game!')
            return self.winner
        # check if the board we are being sent to is complete. If so the player can move anywhere
        if self.get_board(location).winner is None and len(self.get_board(location).get_open_spots()) != 0:
            self.move_anywhere = False
            self.playing_board = copy(location)
        else:
            self.move_anywhere = True
            self.playing_board = -1
        # switch the player's turn
        self.players_turn = self.get_other_player_turn()
        return -1

    # makes a move for the current player using their strategy
    def make_move_strategy(self, verbose = False):
        if self.players_turn == 0:
            location, board = self.strat0.decide_move(self)
            val = self.make_move(location, board, verbose)
            if verbose:
                self.print_board()
            return val
        else:
            location, board = self.strat1.decide_move(self)
            val = self.make_move(location, board, verbose)
            if verbose:
                self.print_board()
            return val

    # return which board are still available to be played on
    def get_open_boards(self):
        return self.open_boards




