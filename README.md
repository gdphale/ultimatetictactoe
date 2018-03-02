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

For: player0=RandomStrat, player1=RandomStrat
```
Mean of player 0 wins is:  0.389978
StdDev of player 0 wins is:  0.00408677329931573
Mean of player 1 wins is:  0.3886470000000001
StdDev of player 1 wins is:  0.004453413409958706
Mean of ties is:  0.221375
StdDev of ties is:  0.0036228545375159623
```

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

###### All other Strategies vs Random

For: player0=WinningStrat, player1=Random
```
Mean of player 0 wins is:  0.81492
StdDev of player 0 wins is:  0.00413129519642
Mean of player 1 wins is:  0.100071
StdDev of player 1 wins is:  0.00321802097569
Mean of ties is:  0.085009
StdDev of ties is:  0.00260557460074
```

For: p0=WinThenNoCenter, p1=Random
```
Mean of  Win then No Center  wins is:  0.805118
StdDev of  Win then No Center  wins is:  0.00441586639291
Mean of  Random  wins is:  0.09763
StdDev of  Win then No Center  wins is:  0.00281902465402
Mean of ties is:  0.097252
StdDev of ties is:  0.00290046479034
```

For: p0=WinTheNoCorners, p1=Random
```
Mean of  Win then No Corners  wins is:  0.405329
StdDev of  Win then No Corners  wins is:  0.00465046868606
Mean of  Random  wins is:  0.505651
StdDev of  Win then No Corners  wins is:  0.00439778341895
Mean of ties is:  0.08902
StdDev of ties is:  0.00302271401227
```

For: p0=Block, p1=Random
```
Mean of player 0 wins is:  0.5628740000000001
StdDev of player 0 wins is:  0.005323450384853792
Mean of player 1 wins is:  0.097518
StdDev of player 1 wins is:  0.0033102078484590655
Mean of ties is:  0.3396080000000001
StdDev of ties is:  0.005009205126564492
```

For: p0=BlockNoCenter, p1=Random
```
Mean of  Block No Center  wins is:  0.560494
StdDev of  Block No Center  wins is:  0.00527469089142
Mean of  Random  wins is:  0.117388
StdDev of  Block No Center  wins is:  0.0036149766251
Mean of ties is:  0.322118
StdDev of ties is:  0.00490331275772
```

For: p0-BlockNoCorners, p1=Random
```
Mean of  Block No Corners  wins is:  0.449725
StdDev of  Block No Corners  wins is:  0.00487976177697
Mean of  Random  wins is:  0.244235
StdDev of  Block No Corners  wins is:  0.00372455030843
Mean of ties is:  0.30604
StdDev of ties is:  0.00438136964887
```


For: p0=WinThenBlock, p1=Random
```
Mean of player 0 wins is:  0.8832449999999998
StdDev of player 0 wins is:  0.003366760312228955
Mean of player 1 wins is:  0.038404
StdDev of player 1 wins is:  0.0018559590512724144
Mean of ties is:  0.078351
StdDev of ties is:  0.0026750885966636694
```

For: p0=WinThenBlockNoCenter, p1=Random
```
Mean of  Win then Block No Center  wins is:  0.877391
StdDev of  Win then Block No Center  wins is:  0.00307977580353
Mean of  Random  wins is:  0.036028
StdDev of  Win then Block No Center  wins is:  0.0017789367611
Mean of ties is:  0.086581
StdDev of ties is:  0.00293184907524
```

For: p0=WinThenBlockNoCorners, p1=Random
```
Mean of  Win then Block No Corners  wins is:  0.641466
StdDev of  Win then Block No Corners  wins is:  0.0054219778679
Mean of  Random  wins is:  0.203493
StdDev of  Win then Block No Corners  wins is:  0.00416953846367
Mean of ties is:  0.155041
StdDev of ties is:  0.00341783835194
```

###### Winning Strategies vs Winning Strategies

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

###### Advanced Winning Strategies vs. Advanced Winning Strategies

For: p0=WinThenBlockNoCornersStrat, p1=WinThenBlockStrat
```
Mean of  Win then Block No Corners  wins is:  0.154532
StdDev of  Win then Block No Corners  wins is:  0.00379085425729
Mean of  Win then Block  wins is:  0.638044
StdDev of  Win then Block No Corners  wins is:  0.00456187066893
Mean of ties is:  0.207424
StdDev of ties is:  0.00362836381858
```

###### Top Strategies against eachother

For p0=winblocknocenter, p1=win
```
Mean of  Win then Block No Center  wins is:  0.618917
StdDev of  Win then Block No Center  wins is:  0.00476525036068
Mean of  Win Board  wins is:  0.252244
StdDev of  Win then Block No Center  wins is:  0.00414469106207
Mean of ties is:  0.128839
StdDev of ties is:  0.00304561635798
```

For: p0=winblocknocenter, p1=winblock
```
Mean of  Win then Block No Center  wins is:  0.386872
StdDev of  Win then Block No Center  wins is:  0.00462897569663
Mean of  Win then Block  wins is:  0.363939
StdDev of  Win then Block No Center  wins is:  0.00483658753668
Mean of ties is:  0.249189
StdDev of ties is:  0.00424694937573
```
