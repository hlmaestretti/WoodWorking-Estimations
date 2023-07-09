#

from Board import Board


class InvalidInput(Exception):
    """
    Raises when an incorrect input is given
    """
    pass


def board_sort(list_of_boards):
    """
    This will be a simple insertion sorting function that uses the length of the board objects and sorts
    them in ascending order. If the width is larger than the width for a board, the two numbers are switched.
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


def convert_list(list_of_cuts):
    """
    The convert_list function converts a list of tuples into a list of boards
    """
    for cut_index, cut in enumerate(list_of_cuts):
        try:
            list_of_cuts[cut_index] = Board(cut[0], cut[1], cut[2])
        except ValueError:
            raise InvalidInput


def canFit(list_of_cuts, boards, saw_thickness=.125, cuts=""):
    """
    The canFit function tests to see if a list of cutouts can fit into the available boards recursively.

    Receives:
        - list_of_cuts  - Array of Board objects that indicate each cut to be done
        - boards        - Array of Board objects that indicates the available wood we have
        - saw_thickness - Default parameter that represents the thickness of the saw blade in inches
        - cuts          - parameter used during the recursive steps
    Returns:
        - If the cuts can fit, it will list out the relative positions of where each cut should be
        - IF they don't fit, it will return False
    """
    
    if cuts == "":
        cuts = ["base"]
        convert_list(list_of_cuts)
        convert_list(boards)
        board_sort(list_of_cuts)
        board_sort(boards)
        if sum([x.get_area() for x in boards]) < sum([y.get_area() for y in list_of_cuts]):
            return False
    
    cut = list_of_cuts[0]
    for index, piece in enumerate(boards):
        if piece.can_fit(cut):
            if len(list_of_cuts) == 1:
                return cuts
            
            possible_cuts = []
            possible_actions = []
            # possible cuts that could be done on the board
            if piece.get_width() >= cut.get_width() and piece.get_length() >= cut.get_length():
                scraps1 = [Board(cut.get_length(), piece.get_width() - cut.get_width(), cut.get_thickness()),
                           Board(piece.get_width(), piece.get_length() - cut.get_length(), cut.get_thickness())
                           ]
                scraps2 = [Board(piece.get_width() - cut.get_width(), piece.get_length(), cut.get_thickness()),
                           Board(cut.get_width(), piece.get_length() - cut.get_length(), cut.get_thickness())
                           ]
                possible_cuts.append(scraps1)
                possible_cuts.append(scraps2)
            if piece.get_width() >= cut.get_length() and piece.get_length() >= cut.get_width():
                scraps3 = [Board(piece.get_width() - cut.get_length(), cut.get_width(), cut.get_thickness()),
                           Board(piece.get_length() - cut.get_width(), piece.get_length(), cut.get_thickness())
                           ]
                scraps4 = [Board(piece.get_width() - cut.get_length(), piece.get_length(), cut.get_thickness()),
                           Board(piece.get_length() - cut.get_width(), cut.get_length(), cut.get_thickness())
                           ]
                possible_cuts.append(scraps3)
                possible_cuts.append(scraps4)

            for possible in possible_cuts:
                will_pop = []
                for ind, scraps in enumerate(possible):
                    if scraps.get_length() <= 0 or scraps.get_width() <= 0:
                        will_pop.append(ind)
                for item in reversed(will_pop):
                    possible.pop(item)

            for i in range(len(possible_cuts)):
                temp = boards[:]
                boards.pop(index)
                boards = boards + possible_cuts[i]
                testing_cuts = canFit(list_of_cuts[1:], boards, saw_thickness,
                                      cuts + [f"cut from ({piece.get_length()}, {piece.get_width()})"])
                boards = temp
                if testing_cuts is not False:
                    # print([(x.get_length(), x.get_width()) for x in boards])
                    return testing_cuts

    return False
