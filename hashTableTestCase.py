from hashTable import Node, LinkedList, HashTable
import unittest

class HashTableTestCase(unittest.TestCase):
    def setUp(self):
        self.hashTable = HashTable(8)

    def test_addCache(self):
        cache = Node(key="fakeUrl", value="fakeImage")
        self.hashTable.insert(cache)
    
    def test_getCache(self):
        self.test_addCache()
        self.assertEqual(self.hashTable.get("fakeUrl"), "fakeImage")
    
    def test_updateCache(self):
        self.test_addCache()
        updatedCache = Node(key="fakeUrl", value="newFakeImage")
        self.hashTable.insert(updatedCache)
        self.assertEqual(self.hashTable.get("fakeUrl"), "newFakeImage")
    
    def test_deleteCache(self):
        self.test_addCache()
        self.hashTable.delete("fakeUrl")
        self.assertIsNone(self.hashTable.get("fakeUrl"))
    
    def test_nonexistentKey(self):
        self.assertIsNone(self.hashTable.get("nonexistentKey"))
    
    def test_collisionHandling(self):
        key1 = "key10000"
        key2 = "keyA"
        value1 = "value1"
        value2 = "value2"
        self.hashTable.insert(Node(key=key1, value=value1))
        self.hashTable.insert(Node(key=key2, value=value2))
        self.assertEqual(self.hashTable.get(key1), value1)
        self.assertEqual(self.hashTable.get(key2), value2)

    def test_collisionFor16Nodes(self):
        for i in range(16):
            self.hashTable.insert(Node(key=f"key{i*10}", value=f"value{i}"))
        for i in range(16):
            self.assertEqual(self.hashTable.get(f"key{i*10}"), f"value{i}") 
    
    def test_deleteNonexistentKey(self):
        self.hashTable.delete("nonexistentKey")
        self.assertIsNone(self.hashTable.get("nonexistentKey")) 
    
    def test_multipleOperations(self):
        keys_values = [("k1", "v1"), ("k2", "v2"), ("k3", "v3")]
        for k, v in keys_values:
            self.hashTable.insert(Node(key=k, value=v))
        for k, v in keys_values:
            self.assertEqual(self.hashTable.get(k), v)
        self.hashTable.delete("k2")
        self.assertIsNone(self.hashTable.get("k2"))
        self.hashTable.insert(Node(key="k2", value="v2_new"))
        self.assertEqual(self.hashTable.get("k2"), "v2_new")

    def test_resize(self):
        N = 40  
        for i in range(N):
            self.hashTable.insert(Node(f"k{i}", i))
        new_buckets = self.hashTable.getBucketSize()
        self.assertGreaterEqual(new_buckets, 10)
        
        for i in range(N):
            self.assertEqual(self.hashTable.get(f"k{i}"), i)

if __name__ == "__main__":
    unittest.main()


