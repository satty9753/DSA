"""
Instructions:
The objective of this assignment is to deepen your understanding of hash tables by implementing a simple cache system. You will create a cache that efficiently stores and retrieves data using a hash table and handles collisions effectively. Implement the cache system from scratch without using Python’s built-in dictionary for the core functionality.
Implement a hash table with the following functionalities:
Put: Insert a key-value pair into the cache.
Get: Retrieve the value associated with a key.
Delete: Remove a key-value pair from the cache.
Implementation Steps:
Step 1: Implement the Node class to store key-value pairs.
Step 2: Implement the LinkedList class for collision handling in the hash table.
Step 3: Implement the HashTable class with methods for insertion, retrieval, and deletion. HashTable class is probably a list of LinkedLists.
Step 4: Write unit tests to verify the functionality of your cache system.
"""
BUCKET_SIZE = 10

class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def update(self, node):
        if not self.head:
            self.head = node
            return
        existedNode = self.find(node.key)
        if existedNode:
            existedNode.value = node.value
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def find(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

    def delete(self, key):
        curr = self.head
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False
    
class Hash(object):
    def __init__(self, bucket):
        # Number of buckets
        self.__bucket = bucket
        # Hash table of size bucket
        self.__table = [LinkedList() for _ in range(bucket)]

    # hash function to map values to key
    def hashFunction(self, node):
        return (hash(node) % self.__bucket)

    def insertItem(self, node):
        # get the hash index of key
        index = self.hashFunction(node)
        self.__table[index].update(node)

    def deleteItem(self, key):
        # get the hash index of key
        index = self.hashFunction(key)
        # Check the key in the hash table
        if not self.__table[index].find(key):
            return
        # delete the key from hash table
        self.__table[index].delete(key)

    # function to display hash table
    def displayHash(self):
        for i in range(self.__bucket):
            print("[%d]" % i, end='')
            for x in self.__table[i]:
                print(" --> %d" % x, end='')
            print()


node = Node("a", 1)
print(hash(node))