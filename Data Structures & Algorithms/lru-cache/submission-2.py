class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=False)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)
            if len(self.cache) > self.cap:
                self.cache.popitem(last=True)
        else:
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)
