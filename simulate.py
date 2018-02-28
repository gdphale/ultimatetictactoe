#!/usr/local/bin/python3

from tictactoe import *
from strategies import *
import matplotlib.pyplot as plt
import numpy as np


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


strat0 = WinAnyBoardStrat()
strat1 = RandomStrat()


# make moves over and over until the game ends. A return value of -1 from the game means the game is not complete
def simulate_game(g, verbose):
    for _ in range(100):
        numb = g.make_move_strategy(verbose = verbose)
        if numb != -1:
            return numb


# returns a dictionary with the different win percentages for strategies
def monte_carlo(x):
    player0wins = 0
    player1wins = 0
    ties = 0
    for _ in range(x):
        # the strategy class is the first strategy made. It simply chooses a random point to go to
        g = Game(strat0 = strat0, strat1 = strat1)
        result = simulate_game(g, False)
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


# print out the results after running monte carlo simuation x times
def print_monte_carlo(x):
    values = monte_carlo(x)
    print('Player 0 win percentage: ', str(values['P0Win']))
    print('Player 1 win percentage: ', str(values['P1Win']))
    print('Tie percentage: ', str(values['Ties']))


# graph the win, lose, and tie percentages for the strategies pinned against eachother
def graph_multiple_monte_carlo(game_runs=1000, monte_carlo_runs=50):
    a = {}
    a['P0Win'] = []
    a['P1Win'] = []
    a['Ties'] = []
    # simulate the games
    for j in range(monte_carlo_runs):
        result = monte_carlo(game_runs)
        a['P0Win'].append(result['P0Win'])
        a['P1Win'].append(result['P1Win'])
        a['Ties'].append(result['Ties'])
    # plot the distributions of the different player's win's
    for key in a:
        h = np.histogram(a[key], bins=11)
        edges = h[1]
        heights = h[0]
        centers = []
        # get the centers from the edges returned from histogram function
        for j in range(len(edges) - 1):
            centers.append( (edges[j] + edges[j+1])/2  )
        plt.bar(centers, heights, width = (edges[1] - edges[0])/2, alpha=0.5, label=str(key))
    print('Mean of player 0 wins is: ', np.mean(a['P0Win']))
    print('StdDev of player 0 wins is: ', np.std(a['P0Win']))
    print('Mean of player 1 wins is: ', np.mean(a['P1Win']))
    print('StdDev of player 1 wins is: ', np.std(a['P1Win']))
    print('Mean of ties is: ', np.mean(a['Ties']))
    print('StdDev of ties is: ', np.std(a['Ties']))
    plt.xlabel('Percentage')
    plt.ylabel('Count')
    plt.title('Histogram of outcomes, ' + str(strat0,) + ' vs ' + str(strat1))
    plt.legend()
    plt.show()


#g = Game(strat0 = strat0, strat1 = strat1)
#simulate_game(g, verbose = True)


#print_monte_carlo(10000)

graph_multiple_monte_carlo(game_runs=10000, monte_carlo_runs=100)


