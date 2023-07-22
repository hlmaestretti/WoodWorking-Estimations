from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import json
import re

app = Flask(__name__)


@app.route('/get_cost', methods=['POST'])
def get_cost():
    # Grab the search criteria from the request
    criteria = request.json['criteria']

    # Append it to the WoodworkersSource URL
    url = f"https://www.woodworkerssource.com/search.html?Search={criteria}"

    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the entire HTML content
        html_content = response.text

        # Use regex to find the "items" list inside the script tag
        pattern = re.compile(r'"items": (\[.*?\])', re.DOTALL)
        matches = pattern.findall(html_content)

        if matches:
            # Get the first match (items_list) from the list of matches
            json_data = matches[0]

            # Parse the JSON data
            try:
                items_list = json.loads(json_data)

                # Now, you can work with the list of items as needed

                # Create a list to store the formatted items
                formatted_items = []
                for item in items_list:
                    # Add each item to the formatted list as a dictionary
                    formatted_item = {
                        "item_name": item["item_name"],
                        "price": item["price"],
                        "quantity": item["quantity"]
                        # Add more fields as needed
                    }
                    formatted_items.append(formatted_item)

                json_response = jsonify(formatted_items)

                # Return the JSON response
                return json_response

            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")


        else:
            print('"items" list not found in the HTML.')
    else:
        print("Failed to fetch the website content.")


if __name__ == '__main__':
    app.run(port=5000)


# # Make the HTTP request to fetch the HTML content
    # response = requests.get(url)
    #
    # # Check if the request was successful
    # if response.status_code == 200:
    #     # Parse the HTML content with Beautiful Soup
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     print(soup)
    #     # Find all elements that contain the pattern "$*.^"
    #     pattern = re.compile(r'\$([\d,]+)\.(\d{2})')
    #
    #     matches = pattern.findall(response.text)
    #
    #     if matches:
    #         # Find all elements that contain the pattern "$*.^"
    #         elements_with_pattern = soup.find_all(text=pattern)
    #
    #         # Iterate through the matches and extract their corresponding text
    #         for price_match, element in zip(matches, elements_with_pattern):
    #             dollars, cents = price_match
    #             price = float(f"{dollars.replace(',', '')}.{cents}")
    #
    #             # Extract the text surrounding the element or its parent element
    #             text = element.parent.text.strip() if element.parent else element.strip()
    #
    #             print("Price:", price)
    #             print("Text:", text)
    #             print()
    #     else:
    #         print("Price not found.")
    # else:
    #     print("Failed to fetch the website content.")