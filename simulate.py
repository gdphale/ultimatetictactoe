from tictactoe import *
from strategies import *


# define the strats to be run with
#
#   strategies are...
#       RandomStrat() - choose a place on the current board
#       NoCenterStrat() - don't move to the center if possible
#       WinCurBoardStrat() - if there is a spot open on the current board to win, place there
#       BlockOpponentStrat() - if your opponent is about to win the current board block them
#       WinThenBlockStrat() - first try and win the curreny board you are platying on, then block the opponent
#       WinThenNoCenterStrat() - first try and win the current board, then if not possible move somewhere randomly that is not the center
#       WinCurBoardAdvancedStrat() - first try and win the current board, then try and setup your next turn to win the board
#

strat0 = WinCurBoardStrat()
strat1 = RandomStrat()


# make moves over and over until the game ends. A return value of -1 from the game means the game is not complete
def simulate_game(g):
    for _ in range(100):
        numb = g.make_move_strategy(verbose = False)
        if numb != -1:
            return numb


def monte_carlo(x):
    player0wins = 0
    player1wins = 0
    ties = 0
    for _ in range(x):
        # the strategy class is the first strategy made. It simply chooses a random point to go to
        g = Game(strat0 = strat0, strat1 = strat1)
        result = simulate_game(g)
        if result == 0:
            player0wins = player0wins + 1
        elif result == 1:
            player1wins = player1wins + 1
        else:
            ties = ties + 1
    values = {}
    values['P0Win'] = player0wins/x
    values['P1Win'] = player1wins/x
    values['Ties'] = ties/x
    return values


def print_monte_carlo(x):
    values = monte_carlo(x)
    print('Player 0 win percentage: ', str(values['P0Win']))
    print('Player 1 win percentage: ', str(values['P1Win']))
    print('Tie percentage: ', str(values['Ties']))


print_monte_carlo(10000)