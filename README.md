# Project Title

A project to simulate ultimate tic tac toe AI's against eachother.

## Getting Started

Pull the code using an ssh key with... 

```
git pull git@github.com:gdphale/ultimatetictactoe.git
```

### Prerequisites

python3.6.3



### Current Strategies

strategies are...
*       RandomStrat() - choose a place randomly
*       NoCenterStrat() - don't move to the center if possible
*       WinAnyBoardStrat() - if you can win a board during a turn, do it
*       BlockOpponentStrat() - if your opponent is about to win, block them
*       WinThenBlockStrat() - first try and win any board then try and block opponent
*       WinThenNoCenterStrat() - first try and win the current board, then if not possible move somewhere randomly that is not the center
*       NoCornersStrat() - move randomly that isn't the corners
*       WinThenNoCornersStrat() - first try and win any board, if we can't then make a move that is not in a corner

### Win Percentages

Matchups:

For: player0=RandomStrat, player1=NoCenterStrat
```
Mean of player 0 wins is:  0.506255
StdDev of player 0 wins is:  0.00473003964043
Mean of player 1 wins is:  0.294336
StdDev of player 1 wins is:  0.00465363341917
Mean of ties is:  0.199409
StdDev of ties is:  0.00416242945886
```
