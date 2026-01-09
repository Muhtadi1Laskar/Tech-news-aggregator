import json
import os
from pathlib import Path


def count_scraped_data():
    base_dir = "./Data/"
    data_folder = [f for f in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, f)) and f.endswith(".json")]

    result = []

    for folder in data_folder:
        try:
            filename = os.path.join(base_dir, folder)
            size = os.path.getsize(filename)

            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)

                result.append({
                    "name": folder,
                    "totalData": len(data) if isinstance(data, list) else 1,
                    "size": size
                })
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except json.JSONDecodeError as e:
            print(f"Error: Failed to decode JSON from '{filename}'. Details: {e}")
        except PermissionError:
            print(f"Error: No permission to read file '{filename}'.")
        except Exception as e:
            print(f"Unexpected error processing '{filename}': {e}")

    return result

if __name__ == "__main__":
    data_counts = count_scraped_data()

    print("\n ------ Data Count Summary -------")

    if data_counts:
        total_items = sum(item["totalData"] for item in data_counts)
        total_size = sum(items["size"] for items in data_counts) * 0.001

        for item in data_counts:
            print(f"{item["name"]}: {item["totalData"]} items")

        print(f"\nTotal files: {len(data_counts)}")
        print(f"Total data items across all files: {total_items}")
        print(f"Total size: {total_size} KB")
    else:
        print("No data files found or empty directory.") 
