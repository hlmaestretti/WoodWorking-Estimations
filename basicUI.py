"""
This file contains a script that creates the basic UI for the program
"""

from canFit import canFit
from woodCutEstimate import woodCutEstimate
from Board import Board
from ast import literal_eval


def end():
    print("Thanks for trying the program!")
    quit()


def convert_str_to_list_tuples():
    exit_flag = True
    while exit_flag:
        list_of_cuts = input("Enter in the following fomrat: (list of tuple of (length, width, thickness)) \n")

        if list_of_cuts == '4':
            end()

        list_of_cuts = literal_eval(list_of_cuts)
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

def intify(str):
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
    print("4. Exit the program")
    print("\n   Please enter the number you would like to try")

    while True:
        answer = input()
        if int(answer) in [1, 2, 3, 4]:
            break
        else:
            print("Error, incorrect entry, try again. Type 4 to quit")

    answer = int(answer)

    if answer == 4:
        end()

    print("Please enter the cuts you want to make.")
    list_of_cuts = convert_str_to_list_tuples()
    if answer == 1:
        for ind, board in enumerate(list_of_cuts):
            list_of_cuts[ind] = Board(board[0], board[1], board[2])

        print("Done, here are the items:")
        for item in list_of_cuts:
            print(f"({item.get_length()}, {item.get_width()}) Board Object: {item}")

    elif answer == 2:
        print("Please enter the wood you have available.")
        list_of_boards = convert_str_to_list_tuples()

        saw_blade = input("Input the thickness of the saw-blade in inches:")
        saw_blade = intify(saw_blade)

        ans = canFit(list_of_cuts, list_of_boards, saw_blade)
        if ans:
            print("It can fit! Here are the cuts:")

            for ind in range(len(ans)):
                print(f"({list_of_cuts[ind].get_length()}, {list_of_cuts[ind].get_width()}), {ans[ind]}")
        else:
            print("It cannot fit!")

    elif answer == 3:
        feed_rate = intify(input("Please enter the feed rate (ft/min)"))

        load_time = intify(input("Please enter the load time (min)"))

        print(f"It will take {round(woodCutEstimate(feed_rate,load_time, list_of_cuts))} minutes!")

    else:
        raise Exception


