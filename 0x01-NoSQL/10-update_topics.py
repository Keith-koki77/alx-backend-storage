#!/usr/bin/env python3
"""
Update topics of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """Returns:The number of documents updated."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
