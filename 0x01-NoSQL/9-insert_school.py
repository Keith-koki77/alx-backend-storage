#!/usr/bin/env python3
"""
Insert a new document into a MongoDB collection based on keyword arguments.
"""


def insert_school(mongo_collection, **kwargs):
    documents = mongo_collection.insert_one(kwargs)
    return documents.inserted_id
