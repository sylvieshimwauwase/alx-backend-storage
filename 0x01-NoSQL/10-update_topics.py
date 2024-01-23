#!/usr/bin/env python3
"""Python script for changing all topics of a school"""

def update_topics(mongo_collection, name, topics):
    """
    Changing all topics of a school documemt
    """

    result = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    print(f"Number of documents updated: {result.modified_count}")
