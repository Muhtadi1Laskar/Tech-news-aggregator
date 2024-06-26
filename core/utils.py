import json
import os

# def save_data(data, website_name):
#     file_path = f"Data/{website_name}.json"

#     with open(file_path, 'a+') as f:
#         print(f.tell())
#         if f.tell() == 0:  # Check if file is empty
#             print("Saved the first page successfully")
#             json.dump(data, f, indent=4) 
#         else:
#             existing_data = json.load(f)
#             print(existing_data)
#             existing_data.extend(data) 
#             f.seek(0) 
#             f.truncate() 
#             json.dump(existing_data, f, indent=4) 

def save_data(data, website_name):
    file_path = f"Data/{website_name}.json"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.extend(data)  # Append new data to the existing list

    with open(file_path, 'w') as f:
        json.dump(existing_data, f, indent=4)