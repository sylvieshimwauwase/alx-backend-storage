#!/usr/bin/env python3
"""python function that returns the list of schools"""

def schools_by_topic(mongo_collection, topic):
    """
    Returning list of schools having a specific topic
    return: a list of schools
    """

    schools_with_topic = list(mongo_collection.find({"topics": topic}))
    return schools_with_topic
