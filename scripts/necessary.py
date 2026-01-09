import json
import os
from pathlib import Path


def count_scraped_data():
    base_dir = "./Data/"
    data_folder = [f for f in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, f)) and f.endswith(".json")]

    result = []

    for filename in data_folder:
        try:
            folder = os.path.join(base_dir, filename)
            size = os.path.getsize(folder)

            with open(folder, 'r', encoding='utf-8') as file:
                data = json.load(file)

                result.append({
                    "name": filename.replace(".json", ""),
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
        total_size_in_bytes = sum(items["size"] for items in data_counts)
        total_size_in_kb = total_size_in_bytes / 1024
        total_size_in_mb = total_size_in_kb / 1024

        for item in data_counts:
            print(f"\n{item["name"]}: {item["totalData"]} items")

        print(f"\nTotal files: {len(data_counts)}")
        print(f"Total data items across all files: {total_items}")
        print(f"Total size: {total_size_in_bytes} BYTES")
        print(f"Total size: {total_size_in_kb} KB")
        print(f"Total size: {total_size_in_mb} MB")
    else:
        print("No data files found or empty directory.") 
