#!/usr/bin/env python3
""" python script to list all documents"""

def list_all(mongo_collection):
    """
    listing all documents
    return: list of all documents
    """
    all_documents = list(mongo_collection.find())
    return all_documents
