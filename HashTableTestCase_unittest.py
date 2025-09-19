from HashTable import Node, LinkedList, HashTable
import unittest
from unittest.mock import patch

class HashTableTestCase(unittest.TestCase):
    def setUp(self):
        self.hashTable = HashTable(10)
    def test_addCache(self):
        cache = Node(key="fakeUrl", value="fakeImage")
        self.hashTable.insert(cache)
        self.assertEqual(self.hashTable.get("fakeUrl"), "fakeImage")

if __name__ == "__main__":
    unittest.main()


