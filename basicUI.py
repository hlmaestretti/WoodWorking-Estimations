"""
This file contains a script that creates the basic UI for the program
"""

from canFit import can_fit
from misc_functions.woodCutEstimate import woodCutEstimate
from misc_functions.Board import Board
from woodCostEstimate import estimator
from ast import literal_eval


def end():
    print("Thanks for trying the program!")
    quit()


def convert_str_to_list_tuples():
    exit_flag = True
    while exit_flag:
        list_of_cuts = input("Enter in the following foemat: (list of tuple of (length, width, thickness)) \n")

        if list_of_cuts == '4':
            end()
        try:
            list_of_cuts = literal_eval(list_of_cuts)
        except ValueError:
            print("Error in input, try again. Enter 4 to quit")
            continue

        if not isinstance(list_of_cuts, list):
            continue
        for index, cut in enumerate(list_of_cuts):
            if isinstance(cut, tuple):
                for num in cut:
                    if isinstance(num, int) or isinstance(num, float):
                        continue
            if index == len(list_of_cuts) - 1:
                exit_flag = False
                break
        if exit_flag:
            print("Error in input, try again. Enter 4 to quit")
            break

    return list_of_cuts


def get_num(str):
    """
    Receives an input and ensures that it is a number
    """
    while True:
        try:
            num = float(str)
            break
        except ValueError:
            print("Error with input, try again")
    return num


if __name__ == "__main__":
    print("Hello! Welcome to my WoodWorking Estimates.\nHere we can do the following things:")
    print("1. Convert a list of cuts in tuple format and convert it to a list of cuts in Board object format")
    print("2. Test to see if a list of cuts can fit into the available wood you have")
    print("3. Get an estimate for how long it will take you to cut your wood")
    print("4. Get an estimate for the cost of the wood.")
    print("5. Exit the program")
    print("\n   Please enter the number you would like to try")

    while True:
        answer = input()
        try:
            answer = int(answer)
            if int(answer) in [1, 2, 3, 4]:
                break
        except ValueError:
            print("Error, incorrect entry, try again. Type 4 to quit")

    if answer == 5:
        end()

    print("Please enter the cuts you want to make.\n")
    list_of_cuts = convert_str_to_list_tuples()
    if answer == 1:
        for ind, board in enumerate(list_of_cuts):
            list_of_cuts[ind] = Board(board[0], board[1], board[2])

        print("Done, here are the items:")
        for item in list_of_cuts:
            print(f"({item.get_length()}, {item.get_width()}) Board Object: {item}")

    elif answer == 2:
        print("Please enter the wood you have available.\n")
        list_of_boards = convert_str_to_list_tuples()

        saw_blade = input("Input the thickness of the saw-blade in inches:\n")
        saw_blade = get_num(saw_blade)

        ans = can_fit(list_of_cuts, list_of_boards, saw_blade)
        if ans:
            print("It can fit! Here are the cuts:")

            for ind in range(len(ans)):
                print(f"({list_of_cuts[ind].get_length()}, {list_of_cuts[ind].get_width()}), {ans[ind]}")
        else:
            print("It cannot fit!")

    elif answer == 3:
        feed_rate = get_num(input("Please enter the feed rate (ft/min)\n"))

        load_time = get_num(input("Please enter the load time (min)\n"))

        print(f"It will take {round(woodCutEstimate(feed_rate,load_time, list_of_cuts))} minutes!")

    elif answer == 4:
        criteria = input("Please enter the type of wood you would like to use.\n")
        thickness = input("Please enter the size of wood you would like. Note give in measure of nominal quarter inches."
                          "Example: .75 inch would be 4/4 You would input 4 for this.\n")
        wood_cost = estimator(list_of_cuts, criteria, thickness)

        print(f"The cost of the wood is estimated to be ${wood_cost}.")
    else:
        raise Exception


