class HashMap:
    def __init__(self, size=100) -> None:
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        hashValue = hash(key) % self.size
        print(hashValue)
        return hashValue
    
    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                print(self.buckets)
                return 
        
        bucket.append((key, value))
        print(self.buckets)


    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for (k, v) in enumerate(bucket):
            if k == key:
                return v
            
nosso_hash = HashMap(20)
nosso_hash.put("Diogo", 20)
nosso_hash.put("diogo", 20)
nosso_hash.put("Enzo", 18)
nosso_hash.put("Hida", 19)
print(nosso_hash.get("Diogo"))
print(nosso_hash.get("Enzo"))
print(nosso_hash.get("Hida"))
nosso_hash.put("Hida", 20)
print(nosso_hash.get("Hida"))

dict = {}



