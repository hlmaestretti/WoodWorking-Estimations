# WoodWorking-Estimations
This package is meant to help with the following woodworking tasks:
  - To figure out if certain cuts of wood can be cut from a single board
  - If possible, to give one method of creating the cuts that you want
  
It accounts for the thickness of the saw blade and it is assumed that the thickness of the wood will no change between cuts. 


## Future Plans
  - Show all possible ways the wood cuts can fit on the board
  - Give the best option based on leaving the largest signle leftover piece 




## Board
This file contains the Board class, which represents a piece of wood that is be used in the program board_cutter to store all needed information for each board.

### Functions and Classes
#### Board 
The class represents a piece of wood with a particular width  and length. It has the following Methods:
  - get_length  - Returns the length of the boar
  - get_width   - Returns the width of the board
  - shift_board - Switches the length and width of the board
  - get_area    - Returns the area of the board
  - can_fit     - Checks to see if another board can be cut from the board. True if it can, false otherwise

## board_cutter
board_cutter is a simple program designed to help the user figure out what cuts can be done on a given board. Currently it only looks to see if there is a way to do the desired cuts on a board, but later it will be optimized to give a more refined cutting pattern to minimize scrap wood.

It is set up as a script to be used quickly.

### Functions and Classes
#### Exceptions: InvalidInput

#### board_sort

#### larger_number
 
#### can_cut_boards_from_board
  
