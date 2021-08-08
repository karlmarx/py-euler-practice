from collections import OrderedDict


class MyLRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, data):
        self.cache[key] = data
        ## in case it was updated and not added:
        self.cache.move_to_end(key) #O(1)
        if len(self.cache) > self.capacity:
            self.cache.pop(last=False) #O(1)

    def __str__(self):
        return f"cap={self.capacity}:\n{self.cache}"
