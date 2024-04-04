#!/usr/bin/env python3
"""module for the class BasicCache"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system that inherits from BaseCaching."""

    def __init__(self):
        """Initializes the cache"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache."""
        return self.cache_data.get(key, None)
