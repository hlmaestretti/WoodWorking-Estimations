"""
The woodCostEstimate program uses the microservice to find the the estimate cost of the wood
for a project.
"""


import json
import requests
from Board import Board, board_sort


def make_request(criteria):
    """
    The make_request function receives a search request and sends it to the microservice where
    the costs will be found of various types of wood.

    Receives:
        - criteria - search parameter to be sent to service
    Returns:
        - list of tuples containing name and cost
    """
    # Define the URL of the Flask application
    url = 'http://127.0.0.1:5000/get_cost'

    # Define the headers with the appropriate content type
    headers = {
        'Content-Type': 'application/json'
    }

    # Create the payload as a dictionary
    payload = {
        'criteria': criteria
    }

    # Convert the payload to JSON
    payload_json = json.dumps(payload)

    # Sending a POST request to the Flask application
    response = requests.post(url, data=payload_json, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Getting the response content and printing it
        data = response.json()

        print(data)
    else:
        # Handle unsuccessful requests
        print(f"Request failed with status code {response.status_code}")


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
        cross_section = thickness * board.get_width()
        board_feet += length_ft * cross_section / 12

    return board_feet


def estimator(list_of_cuts, wood_type, thickness=4) -> float:
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
    criteria = wood_type + " " + str(thickness)
    board_feet = get_total_board_feet(list_of_cuts)
