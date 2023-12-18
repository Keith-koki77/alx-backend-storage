#!/usr/bin/env python3
"""
List all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    documents = list(mongo_collection.find())
    return documents
