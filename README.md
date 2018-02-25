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
#       RandomStrat() - choose a place on the current board
#       NoCenterStrat() - don't move to the center if possible
#       WinCurBoardStrat() - if there is a spot open on the current board to win, place there
#       BlockOpponentStrat() - if your opponent is about to win the current board block them
#       WinThenBlockStrat() - first try and win the curreny board you are platying on, then block the opponent
#       WinThenNoCenterStrat() - first try and win the current board, then if not possible move somewhere randomly that is not the center
#       WinCurBoardAdvancedStrat() - first try and win the current board, then try and setup your next turn to win the board

