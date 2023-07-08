# WoodWorking-Estimations
This package is meant to help with the following woodworking tasks:
  - To figure out if certain cuts of wood can be cut from a single board
  - If possible, to give one method of creating the cuts that you want
  
It accounts for the thickness of the saw blade and it is assumed that the thickness of the wood will no change between cuts. 


## Future Plans
  - Add an estimation tool for cutting time




## Board
This file contains the Board class, which represents a piece of wood that is be used in the program board_cutter to store all needed information for each board.

### Functions and Classes
#### Board 
The class represents a piece of wood with a particular width  and length. It has the following Methods:
  - get_length  - Returns the length of the boar
  - get_width   - Returns the width of the board
  - shift_board - Switches the length and width of the board
  - get_area    - Returns the area of the board
  - get_surface_area - Calculates the surface area of the board
  - get_volume       - Calculates the volume of the board
  - can_fit     - Checks to see if another board can be cut from the board. True if it can, false otherwise

## canFit
This file contains the functions needed to run the canFit function that will check to see if the desired cuts can fit in the available wood
It is set up as a script to be used quickly. Here are the functions
  - InvalidInput - Exception class that handles errors for input
  - board_sort   - Simple sorting method for board objects
  - canFit       - tests to see if a list of cutouts can fit into the available boards recursively

  
