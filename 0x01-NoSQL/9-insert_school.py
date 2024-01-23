#!/usr/bin/env python3
"""python script to insert new document"""

def insert_school(mongo_collection, **kwargs):
    """
    inserting new document into MongoDB
    return: new_id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
