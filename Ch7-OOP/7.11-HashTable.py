class HashTable:
    def __init__(self):
        self.bucket = []

    def put(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key = kv[0]:
                self.bucket[i] = (key, value)
            if not found:
                self.bucket.append((key, value))

    def get(self, key):
        for (k, v) in self.bucket:
            if key == k:
                return v

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
