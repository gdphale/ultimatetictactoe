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
    wins0_plot = []
    wins1_plot = []
    tie_plot = []
    game_plot = []
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
        i = _ + 1
        if i % 100 == 0:
            wins0_plot.append(player0wins/i)
            wins1_plot.append(player1wins/i)
            tie_plot.append(ties/i)
            game_plot.append(i)

    values = {}
    values['P0Win'] = wins0_plot
    values['P1Win'] = wins1_plot
    values['Ties'] = tie_plot
    values['Game'] = game_plot
    return values


# print out the results after running monte carlo simuation x times
def print_monte_carlo(x):
    values = monte_carlo(x)
    print('Player 0 win percentage: ', str(values['P0Win']))
    print('Player 1 win percentage: ', str(values['P1Win']))
    print('Tie percentage: ', str(values['Ties']))


# graph the win, lose, and tie percentages for the strategies pinned against eachother
def graph_multiple_monte_carlo(game_runs=1000, monte_carlo_runs=50):
    # simulate the games
    fig, ax = plt.subplots(3, figsize=(9, 6))
    for j in range(monte_carlo_runs):
        a = monte_carlo(game_runs)
        ax[0].plot(a['Game'], a['P0Win'], linewidth=1.5)
        ax[1].plot(a['Game'], a['P1Win'], linewidth=1.5)
        ax[2].plot(a['Game'], a['Ties'], linewidth=1.5)
    ax[0].set_title("Convergence graph: " + str(strat0) + " vs " + str(strat1))
    ax[0].set_ylabel("P0 winning %")
    ax[1].set_ylabel("P1 winning %")
    ax[2].set_ylabel("Tie %")
    ax[2].set_xlabel("Game")
    plt.show()

#g = Game(strat0 = strat0, strat1 = strat1)
#simulate_game(g, verbose = True)


#print_monte_carlo(10000)

graph_multiple_monte_carlo(game_runs=40000, monte_carlo_runs=25)


