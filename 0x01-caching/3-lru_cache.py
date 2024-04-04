#!/usr/bin/env python3
"""module for the class LRUCache"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """A LRU caching system that inherits from BaseCaching."""

    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Adds an item to the cache.
        When cache is full, discards in LRU
        """
        if key and item:
            if self.get(key) != item:
                self.cache_data[key] = item
                if key not in self.keys:
                    self.keys.append(key)
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    self.cache_data.pop(self.keys[0])
                    print('DISCARD:', self.keys[0])
                    self.keys.pop(0)

    def get(self, key):
        """Retrieves an item from the cache."""
        value = self.cache_data.get(key, None)
        if value:
            self.keys.remove(key)
            self.keys.append(key)
        return value
