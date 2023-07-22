
import json
import requests


def make_request(criteria):
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


if __name__ == '__main__':
    criteria = "walnut"
    make_request(criteria)
