"""
Cache Operations - Advanced Level

Advanced caching implementations with recursive helper methods.
"""


class LRUCache:
    """3. LRU Cache with recursive helper methods
    
    Least Recently Used (LRU) Cache implementation that uses recursive
    methods for internal operations.
    
    Args:
        capacity (int): Maximum number of items the cache can hold
        
    Example:
        >>> lru = LRUCache(2)
        >>> lru.put(1, 1)
        >>> lru.put(2, 2)
        >>> lru.get(1)  # Returns 1
        1
        >>> lru.put(3, 3)  # Evicts key 2
        >>> lru.get(2)  # Returns -1 (not found)
        -1
    """
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []
    
    def _remove_from_order(self, key, index=0):
        """Recursively remove key from order list
        
        Args:
            key: Key to remove
            index (int): Current index to check (default: 0)
        """
        if index >= len(self.order):
            return
        if self.order[index] == key:
            self.order.pop(index)
            return
        self._remove_from_order(key, index + 1)
    
    def get(self, key):
        """Get value for key and mark as recently used
        
        Args:
            key: Key to retrieve
            
        Returns:
            int: Value for key or -1 if not found
        """
        if key not in self.cache:
            return -1
        
        self._remove_from_order(key)
        self.order.append(key)
        return self.cache[key]
    
    def put(self, key, value):
        """Put key-value pair in cache
        
        Args:
            key: Key to store
            value: Value to store
        """
        if key in self.cache:
            self._remove_from_order(key)
        elif len(self.cache) >= self.capacity:
            lru = self.order.pop(0)
            del self.cache[lru]
        
        self.cache[key] = value
        self.order.append(key)