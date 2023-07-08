# This file contains the Board class, which represents a piece of wood that will be used in the program 
# cutting_some_boards

class Board:
    """
    The Board class represents a piece of wood with a particular width and length. It has the following 
    private data members and methods:
    
    Private Data Members:
        - length - The length of the piece of wood
        - width  -  The width of the piece of wood
        
    Methods:
        - get_length  - Returns the length of the board
        - get_width   - Returns the width of the board
        - shift_board - Switches the length and width of the board
        - get_area    - Returns the area of the board
        - can_fit     - Checks to see if another board can be cut from the board. True if it can, false
                        otherwise
    """
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    def get_length(self):
        """
        The get_length method returns the length of the board.
        
        Return:
            length
        """
        return self._length
    
    def get_width(self):
        """
        The get_width method returns the width of the board.
        
        Return:
            Width
        """
        return self._width
    
    def shift_board(self):
        """
        The shift_board method switches the width and length of the board.
        
        Returns:
            None
        """
        temp = self._length
        self._length = self._width
        self._width = temp
    
    def get_area(self):
        """
        The get_area returns the area of the board by doing the caluclation length * width.
        
        Return:
            Area of the board
        """
        return self._length * self._width
    
    def can_fit(self, another_board):
        """
        The can_fit methods checks to see if another board can be cut from this board. It does
        so by comparing the lengths and widths of each board to see if it is possible.
        
        Return:
            Boolean - True if it is possible
                    - False if it is not
        """
        if self._length >= another_board.get_length():
            if self._width >= another_board.get_width():
                return True
        
        if self._width >= another_board.get_length():
            if self._length >= another_board.get_width():
                return True
            
        return False
