from flask import request, jsonify
import requests
import json
import re


def get_cost(criteria):

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
                        "price": item["price"]
                    }
                    formatted_items.append(formatted_item)

                return formatted_items

            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")

        else:
            print('"items" list not found in the HTML.')
    else:
        print("Failed to fetch the website content.")

