
    # 1. HashMap: key -> linked_list node
    # 2, Doubly listed list: LRU <-> ... <-> MRU
    # 3. get:
    #       - if missing -> -1
    #       - otherise, move node to MRU and return the value
    # 4. put:
    #       - update existing node or create a new node
    #       - move it MRU
    #       - if over capacity, remove LRU
    #5. Dummy left/right nodes simplify insert/remove

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value

        return value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)