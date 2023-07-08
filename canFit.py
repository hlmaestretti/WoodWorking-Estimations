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

def larger_number(num1, num2):
    """
    larger_number is a simple compare function that returns the larger of two numbers. It returns the second
    number if they are the same size.
    """
    if num1 > num2:
        return num1

    return num2
    
def can_cut_boards_from_boards(list_of_cuts, boards, saw_thickness, cuts = ""):
    """
    This will act recursively to find the see if all the list of cuts can be done on the given boards.

    First set cuts up to be a list and maybe organize list

    see if first cut fits on one of the boards.
        if it does, then cut that board into 3 pieces (the desired cut and the 2 scraps). when calling itself, add the
        variations of the scrap and delete the board that was used. This gives two recursive calls

        if it doesn't fit the first, continue to the next

        if it doesn't fit any, then return false

    end recursion when either the list_of_cuts is empty or a piece is found that cannot fit onto any board, return false
    """
    
    if cuts == "":
        cuts = ["base"]
        board_sort(list_of_cuts)
        board_sort(boards)
    
    cut = list_of_cuts[0]
    for index, piece in enumerate(boards):
        if piece.can_fit(cut):
            if len(list_of_cuts) == 1:
                return cuts
            
            possible_cuts = []
            possible_actions = []
            # possible cuts that could be done on the board
            if piece.get_width() >= cut.get_width() and piece.get_length() >= cut.get_length():
                scraps1 = [Board(cut.get_length(), piece.get_width() - cut.get_width()),
                           Board(piece.get_width(), piece.get_length() - cut.get_length())
                           ]
                scraps2 = [Board(piece.get_width() - cut.get_width(), piece.get_length()),
                           Board(cut.get_width(), piece.get_length() - cut.get_length())
                           ]
                possible_cuts.append(scraps1)
                possible_cuts.append(scraps2)
                possible_actions.append("Horizontal")
                possible_actions.append("Horizontal")
            if piece.get_width() >= cut.get_length() and piece.get_length() >= cut.get_width():
                scraps3 = [Board(piece.get_width() - cut.get_length(), cut.get_width()),
                           Board(piece.get_length() - cut.get_width(), piece.get_length())
                           ]
                scraps4 = [Board(piece.get_width() - cut.get_length(), piece.get_length()),
                           Board(piece.get_length() - cut.get_width(), cut.get_length())
                           ]
                possible_cuts.append(scraps3)
                possible_cuts.append(scraps4)
                possible_actions.append("Vertical")
                possible_actions.append("Vertical")
                
            for i in range(len(possible_cuts)):
                temp = boards[:]
                boards.pop(index)
                boards = boards + possible_cuts[i]
                testing_cuts = can_cut_boards_from_boards(list_of_cuts[1:], boards, saw_thickness,
                                                          cuts + [possible_actions[i]])
                boards = temp
                if testing_cuts is not False:
                    return testing_cuts

    return False


if __name__ == "__main__":
    print("Please give the dimensions of the boards you want to cut one at a time. Leave blank if you are done."
          "Format: length,width")
    list_cuts = [(11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1),
                 (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1),
                 (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1),
                 (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1), (11.5, 1),
                 (40, .75)]
    list_boards = [(48, 9)]

    print(list_cuts)
    # while True:
    #     item = input()
    #     if item == "":
    #         break
    #     nums = item.split(",")
    #     list_boards.append((float(nums[0]), float(nums[1])))

    for cut_index, cut in enumerate(list_cuts):
        try:
            list_cuts[cut_index] = Board(cut[0], cut[1])
        except ValueError:
            raise InvalidInput

    for board_index, board in enumerate(list_boards):
        try:
            list_boards[board_index] = Board(board[0], board[1])
        except ValueError:
            raise InvalidInput

    board_sort(list_cuts)
    board_sort(list_boards)

    # board_to_be_cut = input("Please give me the size of the board that will be cut in the format (length, width)")
    # temp_item = board_to_be_cut.split(",")
    # board_to_be_cut = Board(float(temp_item[0]), float(temp_item[1]))
    #
    # if not isinstance(board_to_be_cut, Board):
    #     raise InvalidInput

    saw_blade = float(input("Please give me the thickness of the saw blade (typical is .125 in)."
                            " Please give number in inches."))

    if not isinstance(saw_blade, (int, float)):
        raise InvalidInput

    test = can_cut_boards_from_boards(list_cuts, list_boards, saw_blade)
    if not test:
        print("The pieces you requested cannot all fit on this board!")

    else:
        print("The pieces you requested can all fit on this board! The cuts are as follows:")
        for cut_index in range(len(test)):
            print((list_cuts[cut_index].get_length(), list_cuts[cut_index].get_width()), test[cut_index])
