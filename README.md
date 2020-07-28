# Conway's Game Of Life

Python Implementation Of Conway's Game Of Life

**_About_** :

The Conway's Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

The rules of the game are as follows:

1) Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2) Any live cell with two or three live neighbours lives on to the next generation.
3) Any live cell with more than three live neighbours dies, as if by overpopulation.
4) Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

**The Game of Life is undecidable, which means that given an initial pattern and a later pattern, no algorithm exists that can tell whether the later pattern is ever going to appear. This is a corollary of the halting problem: the problem of determining whether a given program will finish running or continue to run forever from an initial input.**

**For more information and interesting patterns to use: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life**  

**_conway.py_** :


On opening, enter then number of columns(max:35) and enter the number of rows(max:100). Then choose the mode of display:
1) Continuous: (The display will be updated automatically in 0.1 seconds)
2) Non-Continuous: (User has to manually press enter for every display update, hence can see the growth/destruction of cells step by step, and also can reset the board by entering '+')

Then the user has to enter the X Position, then enter the Y-Position of the live cell. On Entering '+' the computer will randomly insert live cells for you by taking the number of live cells to be inserted as an input. Leave The X Position blank and press enter when done.

*Red Color: Dead Cell, Green Color: Live Cell*

	
