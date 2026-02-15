import re
import os
import json
import logging
from dateutil import parser
from fetch import fetch_html
from bs4 import BeautifulSoup
from configparser import ParsingError
from datetime import datetime, timezone
from typing import Any, Dict, List, Union

from model.database import read_article

# Optional: Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_to_json(data: Any, filename: str, output_dir: str = "Data") -> str:
    """
    Save data to a JSON file. Appends to existing data or creates new file.

    Args:
        data: The data to save (dict, list, or any JSON-serializable object)
        filename: Name of the JSON file (with or without .json extension)
        output_dir: Directory to save the file in (default: "Data")

    Returns:
        str: Full path to the saved file

    Raises:
        TypeError: If data is not JSON-serializable
        PermissionError: If cannot write to the file
    """
    try:
        # Ensure filename ends with .json
        if not filename.lower().endswith(".json"):
            filename = f"{filename}.json"

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Create full file path
        filepath = os.path.join(output_dir, filename)

        # Initialize existing_data as empty list
        existing_data = []

        # Check if file exists and is not empty
        if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
            try:
                with open(filepath, "r", encoding="utf-8") as json_file:
                    existing_data = json.load(json_file)

                    # Ensure existing_data is a list
                    if not isinstance(existing_data, list):
                        # If existing data is not a list, wrap it in a list
                        existing_data = [existing_data]
                        logger.warning(
                            f"Existing data in {filename} was not a list. Converted to list."
                        )

            except json.JSONDecodeError as e:
                logger.warning(
                    f"Could not parse JSON in {filename}: {e}. Starting with empty list."
                )
                existing_data = []
            except Exception as e:
                logger.warning(
                    f"Error reading {filename}: {e}. Starting with empty list."
                )
                existing_data = []

        # Process the new data
        if isinstance(data, list):
            # If data is a list, extend the existing list
            existing_data.extend(data)
        else:
            # If data is a single item, append it
            existing_data.append(data)

        # Save the combined data back to file
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2, default=str)

        logger.info(f"Data saved to {filepath}. Total items: {len(existing_data)}")
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


def get_last_run_index():
    base_dir = "Data"
    file_path = os.path.join(base_dir, "runStats.json")

    os.makedirs(base_dir, exist_ok=True)

    if not os.path.exists(file_path):
        try:
            with open(file_path, "w") as f:
                json.dump([], f, indent=4)
            return 0
        except IOError as e:
            print(f"Error creating file: {e}")
            return 0

    try:
        with open(file_path, "r") as f:
            data = json.load(f)

            if isinstance(data, list) and len(data) > 0:
                last_entry = data[-1]
                if isinstance(last_entry, dict):
                    return last_entry.get("run_index", 0)

            return 0

    except json.JSONDecodeError as e:
        logger.warning(f"Could not parse JSON in {file_path}: {e}. Returning 0.")
        return 0
    except Exception as e:
        logger.warning(f"Error reading {file_path}: {e}. Returning 0.")
        return 0


def dedupe(articles):
    seen = set()
    unique = []

    for a in articles:
        key = a["id"]

        if key not in seen:
            seen.add(key)
            unique.append(a)

    return unique


def convert_to_epoch(value):
    if value is None:
        return None

    if isinstance(value, (int, float)) or str(value).isdigit():
        value = int(value)

        if value > 10_000_000_000:
            return value // 1000

        return value

    try:
        dt = parser.parse(value)

        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)

        return int(dt.timestamp())

    except Exception:
        return None


def get_epoch_time():
    return int(datetime.now(timezone.utc).timestamp())


def remove_tag_from_text(text):
    clean_text = re.sub(r'</?[pP]>', '', text)
    return clean_text.strip()


def clean_text(text):
    text = text.replace("\n", " ")
    return " ".join(text.split()).strip()


def parse_article(slug, link): #div.mt-3 article p 
    all_papers = {
        "Amar Desh": {
            "selector": "div[class='block-full_richtext'] p",
            "index": 5
        },
        "Daily Noya Diganta": {
            "selector": "div[class='post-body'] div p",
            "index": 5
        },
        "Daily Sangram": {
            "selector": "div[class='post-content'] div div p",
            "index": 5
        },
        "Bonik Bartha (Bangla)": {
            "selector": "div[class='post-body']  div ",
            "index": 1
        },
        "The Business Standard (Bangla)": {
            "selector": "div[class='section-content margin-bottom-2'] p",
            "index": 1
        },
        "Bangladesh Pratidin": {
            "selector": "div.mt-3 article",
            "index": 2
        }

    }

    paper = all_papers.get(slug, "")
    if not paper:
        raise ValueError(f"Unsupported paper: {slug}")
    
    selector = paper.get("selector", "")
    total_sentence = paper.get("index", "")

    html_content = fetch_html(link)
    if not html_content:
        raise ParsingError("Failed to fetch article HTML")
    soup = BeautifulSoup(html_content, "html.parser")

    article_body = soup.select(selector)
    if not article_body:
        raise ParsingError("The article layout changed")
    
    # first_few_lines = article_body[0:total_sentence] # Selecting the text of the first 3 paragraph
    first_few_lines = article_body
    text = [clean_text(p.get_text(strip=True)) for p in first_few_lines]

    return " ".join(text)


def clean_rss_paragraph_text(html_string):
    """
    Extract text from HTML string by removing all HTML tags.
    
    Args:
        html_string (str): Input string containing HTML
    
    Returns:
        str: Clean text with all HTML tags removed
    """
    # Pattern to match any HTML tag including self-closing tags
    tag_pattern = r'<[^>]+>'
    
    # Remove all HTML tags
    text_only = re.sub(tag_pattern, '', html_string)
    
    # Clean up extra whitespace (multiple spaces/newlines/tabs)
    # Replace multiple whitespace with single space and strip
    text_only = re.sub(r'\s+', ' ', text_only).strip()
    
    return text_only


class EmptyArticleError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return f"Empty Article from {self.message}'s rss feed"