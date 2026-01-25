import os
from dotenv import load_dotenv
from pymongo import MongoClient, UpdateOne

load_dotenv()

database_url = os.getenv("DATABASE_URL_LOCAL")
database_name = os.getenv("DATABASE_NAME")
collection_name = os.getenv("DATABASE_COLLECTION")

client = MongoClient(database_url)
db = client[database_name]
collections = db[collection_name]


def save_to_database(articles):
    if not articles:
        return None

    operations = []

    for article in articles:
        operations.append(
            UpdateOne(
                {"_id": article["id"]},
                {
                    "$setOnInsert": {
                        "_id": article["id"],
                        "createdAt": article["fetchedDate"],
                        "sortDate": article["sortDate"],
                        "publishedDate": article["publishedDate"],
                        "url": article["url"],
                        "source": article["source"],
                        "language": article["language"],
                        "dateSource": article["dateSource"],
                        "paragraph": article["paragraph"]
                    },
                    "$set": {
                        "title": article["title"],
                        "category": article["category"],
                        "contentHash": article["contentHash"],
                        "lastSeenAt": article["fetchedDate"],
                    },
                },
                upsert=True,
            )
        )

    try:
        result = collections.bulk_write(operations, ordered=True)
        print(
            {
                "inserted": result.upserted_count,
                "updated": result.modified_count,
                "matched": result.matched_count,
            }
        )

        return {
            "inserted": result.upserted_count,
            "updated": result.modified_count,
            "matched": result.matched_count,
        }
    except Exception as e:
        print(f"An error occured: {e}")


def read_article(query, projection_fields  = {}):
    if not (isinstance(query, dict) or isinstance(projection_fields , dict)):
        print("Invalid query. Query must be dictionary")
        return
    
    try:
        result = collections.find(query, projection_fields )

        return result
    except Exception as e:
        print(f"Failed to read data from the database: {e}")
