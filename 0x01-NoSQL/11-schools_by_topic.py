#!/usr/bin/env python3
"""
Return the list of schools having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """Returns:A list of school documents matching the specified topic."""
    return mongo_collection.find({"topics": topic})
