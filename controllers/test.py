import json

# Open the JSON file in append mode
with open("users.json", "a") as f:
    while True:
        # Prompt the user for their name and surname
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")

        # Create a dictionary with the user's name and surname
        user_data = {'name': name, 'surname': surname}

        # Use the json.dump() function to save the dictionary to the file
        json.dump(user_data, f)
        # Add a newline character after the dictionary to separate it from the next one
        f.write('\n')

        # Prompt the user to enter more data or exit the loop
        more = input("Enter more data (y/n)? ")
        if more.lower() != 'y':
            break
