import json
import os
from datetime import datetime
from typing import Any, Dict, List, Union
import logging

# Optional: Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_to_json(data: Any, filename: str) -> str:
    output_dir = "Data"
    """
    Save data to a JSON file.
    
    Args:
        data: The data to save (dict, list, or any JSON-serializable object)
        filename: Name of the JSON file (without .json extension)
        output_dir: Directory to save the file in (default: "data")
    
    Returns:
        str: Full path to the saved file
    
    Raises:
        TypeError: If data is not JSON-serializable
        PermissionError: If cannot write to the file
    """
    try:
        # Ensure filename ends with .json
        if not filename.lower().endswith('.json'):
            filename = f"{filename}.json"
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create full file path
        filepath = os.path.join(output_dir, filename)
        
        # Save data to JSON file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        
        logger.info(f"Data saved to {filepath}")
        return filepath
        
    except (TypeError, json.JSONDecodeError) as e:
        logger.error(f"Data is not JSON-serializable: {e}")
        raise TypeError(f"Data is not JSON-serializable: {e}")
    except PermissionError as e:
        logger.error(f"Permission denied: {e}")
        raise
    except Exception as e:
        logger.error(f"Error saving JSON file: {e}")
        raise



def dedupe(articles):
    seen = set()
    unique = []

    for a in articles:
        key = a["url"]

        if key not in seen:
            seen.add(key)
            unique.append(a)

    return unique