import json

# Initialize an empty set to store unique email addresses
unique_emails = set()

# Open and load the JSON file with error handling
try:
    with open('csvjson.json', 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)

        # Extract email addresses from each record in the data
        for record in data:
            if 'email' in record:
                unique_emails.add(record['email'])

except FileNotFoundError:
    print("Error: The file 'csvjson.json' was not found.")
except json.JSONDecodeError:
    print("Error: Failed to decode the JSON file.")
except Exception as e:
    print(f"An error occurred: {e}")

# Print the unique email addresses and their count
print("Unique Emails:", unique_emails)
print("Total Unique Emails:", len(unique_emails))
