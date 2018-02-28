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

###### Basic Variations

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

For: player0=NoCorners, player1=Random
```
Mean of  No Corners  wins is:  0.243091
StdDev of  No Corners  wins is:  0.00400397539952
Mean of  Random  wins is:  0.669355
StdDev of  No Corners  wins is:  0.00452847380472
Mean of ties is:  0.087554
StdDev of ties is:  0.00248146811384
```

For: player0=nocenter, player1=nocorner
```
Mean of  No Center  wins is:  0.487039
StdDev of  No Center  wins is:  0.0043193493723
Mean of  No Corners  wins is:  0.404806
StdDev of  No Center  wins is:  0.0042262470349
Mean of ties is:  0.108155
StdDev of ties is:  0.00276782857128
```

###### Winning Strategies + Basic Variations

For: player0=WinningStrat, player1=Random
```
Mean of player 0 wins is:  0.81492
StdDev of player 0 wins is:  0.00413129519642
Mean of player 1 wins is:  0.100071
StdDev of player 1 wins is:  0.00321802097569
Mean of ties is:  0.085009
StdDev of ties is:  0.00260557460074
```

For: player0=WinNoCenters, player1=WinNoCorners
```
Mean of  Win then No Center  wins is:  0.847726
StdDev of  Win then No Center  wins is:  0.00406796312668
Mean of  Win then No Corners  wins is:  0.110197
StdDev of  Win then No Center  wins is:  0.00328443160988
Mean of ties is:  0.042077
StdDev of ties is:  0.00210973244749
```


For: player0=WinAnyBoard, player1=WinAnyBoardThenNoCorners
```
Mean of  Win Board  wins is:  0.852629
StdDev of  Win Board  wins is:  0.00372059927969
Mean of  Win then No Corners  wins is:  0.112776
StdDev of  Win Board  wins is:  0.00323391774787
Mean of ties is:  0.034595
StdDev of ties is:  0.00198923980455
```

For: player0=WinAnyBoard, player1=WinThenNoCenter
```
Mean of  Win Board  wins is:  0.457647
StdDev of  Win Board  wins is:  0.00472248779776
Mean of  Win then No Center  wins is:  0.436746
StdDev of  Win Board  wins is:  0.0046335390362
Mean of ties is:  0.105607
StdDev of ties is:  0.00290135330493
```
