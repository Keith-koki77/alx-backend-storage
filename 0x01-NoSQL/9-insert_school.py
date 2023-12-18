#!/usr/bin/env python3
"""
Insert a new document into a MongoDB collection based on keyword arguments.
"""


def insert_school(mongo_collection, **kwargs):
    """ The new _id of the inserted document."""
    documents = mongo_collection.insert_one(kwargs)
    return documents.inserted_id
