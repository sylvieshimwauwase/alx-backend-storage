#!/usr/bin/env python3
"""python scripts that provides some stats about nginx logs in MongoDB"""
import pymongo


def connect_to_mongodb():
    """function that connects server"""
    client = pymongo.MongoClient("mongodb://localost:27017/")

    db = client['logs']

    collection = db['nginx']

    return collection

def get_logs_count(collection):

    return collection.count_documents({})


def get_method_counts(collection):
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}
    return method_counts

def get_stt_endpoint_count(collection):
    return collection.count_documents({"method": "GET", "path": "/status"})

def main():
    # Connect to MongoDB
    nginx_collection = connect_to_mongodb()

    # Get total logs count
    logs_count = get_logs_count(nginx_collection)
    print(f"{logs_count} logs where {logs_count} is the number of documents in this collection")

    # Get method counts
    method_counts = get_method_counts(nginx_collection)
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\t{count} logs with method={method}")

    # Get count for method=GET and path=/status
    status_endpoint_count = get_stt_endpoint_count(nginx_collection)
    print(f"{status_endpoint_count} logs with method=GET and path=/status")

if __name__ == "__main__":
    main()