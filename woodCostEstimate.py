"""
The woodCostEstimate program uses the microservice to find the the estimate cost of the wood
for a project.
"""

from misc_functions.Board import Board, get_total_board_feet
from misc_functions.get_price import get_cost


class RequestError(Exception):
    """
    This is a custom error for when the request fails
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def estimator(list_of_cuts, wood_type, thickness='4') -> float:
    """
    The estimator uses the data given to estimate the cost of buying the wood needed for this project.
    It sends the list_of_cuts to a board foot calculator and then finds the cost of the wood by using
    a requestor. Once these are found it returns the estimated cost.

    Receives:
        - list_of_cuts - A list of Board objects
        - wood_type    - The wood you are type to find the cost of
        - thickness    - The size of wood given in quarters. 4 would be 4/4 or nominal 1 inch.
    Returns:
        - Cost estimate of the wood in USD
    """
    for ind, board in enumerate(list_of_cuts):
        list_of_cuts[ind] = Board(board[0], board[1], board[2])

    criteria = wood_type + " " + thickness
    board_feet = get_total_board_feet(list_of_cuts)
    list_of_options = get_cost(criteria)

    if list_of_options == 0:
        raise RequestError("Server failed to return data")

    price = 0

    for option in list_of_options:
        if "lumber" in option["item_name"].lower():
            price = option["price"]
            break

    if price == 0:
        raise RequestError("Request did not receive the price of any lumber.")

    return round(1.3 * price * board_feet, 2)

