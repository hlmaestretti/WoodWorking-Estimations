"""
This file contains the Board class, which represents a piece of wood that will be used in the program
cutting_some_boards
"""


class Board:
    """
    The Board class represents a piece of wood with a particular width and length. It has the following 
    private data members and methods:
    
    Private Data Members:
        - length - The length of the piece of wood
        - width  -  The width of the piece of wood
        
    Methods:
        - get_length       - Returns the length of the board
        - get_width        - Returns the width of the board
        - shift_board      - Switches the length and width of the board
        - get_area         - Returns the area of the board
        - get_surface_area - Calculates the surface area of the board
        - get_volume       - Calculates the volume of the board
        - can_fit          - Checks to see if another board can be cut from the board. True if it can, false
                             otherwise
    """
    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self._thickness = thickness
    
    def get_length(self):
        """
        The get_length method returns the length of the board.
        """
        return self._length
    
    def get_width(self):
        """
        The get_width method returns the width of the board.
        """
        return self._width

    def get_thickness(self):
        """
        The get_thickness method returns the thickness of the board.
        """
        return self._thickness
    
    def shift_board(self):
        """
        The shift_board method switches the width and length of the board.
        
        Returns:
            - None
        """
        temp = self._length
        self._length = self._width
        self._width = temp
    
    def get_area(self):
        """
        The get_area returns the area of the face of the board by doing the calculation length * width.
        
        Return:
            - Area of the board
        """
        return self._length * self._width

    def get_surface_area(self):
        """
        The get_surface_area method calculates the surface area of the whole board. by using the following
        equation:  SA = 2(length*width) + 2(length*thickness) + 2(width*thickness)

        Return:
            - Surface Area of the board
        """
        l = self._length
        w = self._width
        t = self._thickness
        return 2*(l*w) + 2*(l*t) + 2*(w*t)

    def get_volume(self):
        """
        The get_volume method calculates the volume of the board by using the following equation:
        v = length*width*thickness

        Return:
            - Volume of the board
        """
        return self._length * self._width * self._thickness

    def can_fit(self, another_board):
        """
        The can_fit methods checks to see if another board can be cut from this board. It does
        so by comparing the lengths and widths of each board to see if it is possible.
        
        Return:
            Boolean - True if it is possible
                    - False if it is not
        """
        if self._thickness >= another_board.get_thickness():
            if self._length >= another_board.get_length():
                if self._width >= another_board.get_width():
                    return True

            if self._width >= another_board.get_length():
                if self._length >= another_board.get_width():
                    return True
            
        return False


def board_sort(list_of_boards):
    """
    This will be a simple insertion sorting function that uses the length of the board objects and sorts
    them in ascending order. If the width is larger than the length of a given board, the two numbers are switched.
    """
    for index in range(1, len(list_of_boards)):
        board = list_of_boards[index]
        if board.get_length() < board.get_width():
            board.shift_board()

        pos = index - 1
        while pos >= 0 and list_of_boards[pos].get_length() < board.get_length():
            list_of_boards[pos + 1] = list_of_boards[pos]
            pos -= 1
        list_of_boards[pos + 1] = board


def get_total_board_feet(list_of_cuts, thickness=4) -> float:
    """
    The get_total_volume function calculates the total board feet of the list of cuts.
    A board foot is 144 in^3 of wood. It is usually given in the format of length as if it had a
    cross-section of 12 in^2. So if a board has a cross-section of 6 in^2 then one board foot
    would be 2 feet long

    Receives:
        - List of board objects
    Returns:
        -board feet of list
    """
    board_sort(list_of_cuts)
    board_feet = 0

    for board in list_of_cuts:
        length_ft = board.get_length() / 12
        cross_section = thickness / 4 * board.get_width()
        board_feet += length_ft * cross_section / 12

    return board_feet