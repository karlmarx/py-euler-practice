class HashMap:
    def __init__(self, size:int):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def put(self, key: int, value):
        index = hash(key) % self.size
        bucket = self.hash_table[index]

        record = (key, value)

        record_found = False
        for node in bucket:
            if node[0] == key:
                node = (key,value)


        if not self.hash_table[index]:
            self.hash_table[index].append()