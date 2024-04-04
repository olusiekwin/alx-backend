#!/usr/bin/env python3
"""module for the class LIFOCache"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """A LIFO caching system that inherits from BaseCaching."""

    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.last = None

    def put(self, key, item):
        """
        Adds an item to the cache.
        When cache is full, discards in LIFO
        """
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.cache_data.pop(self.last)
                    print('DISCARD:', self.last)
                self.last = key

    def get(self, key):
        """Retrieves an item from the cache."""
        return self.cache_data.get(key, None)
