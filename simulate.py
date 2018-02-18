from tictactoe import *

# the strategy class is the first strategy made. It simply chooses a random point to go to
g = Game(strat0 = Strategy(), strat1 = Strategy())

# make moves over and over until the game ends. A return value of -1 from the game means the game is not complete
for _ in range(100):
    numb = g.make_move_strategy(verbose = True)
    if numb != -1:
        break

