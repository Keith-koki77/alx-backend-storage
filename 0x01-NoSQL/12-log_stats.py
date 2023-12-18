#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def nginx_logs_stats('mongodb://127.0.0.1:27017'):
     """script that provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\t{count} {method} requests")

    specific_request_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"\t{specific_request_count} GET requests to /status")

    client.close()
