class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def update(self, node):
        prev = None
        curr = self.head
        while curr:
            if curr.key == node.key:
                curr.value = node.value
                return False
            prev = curr
            curr = curr.next
        newNode = Node(node.key, node.value, next=None)
        if self.head is None:
            self.head = newNode
        else:
            prev.next = newNode
        return True

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
    
class HashTable(object):
    def __init__(self, bucket):
        # Number of buckets
        self.__bucket = bucket
        # Hash table of size bucket
        self.__table = [LinkedList() for _ in range(bucket)]
        self.maxinumLoadFactor = 0.75
        self.minimumLoadFactor = 0.25
        self.__size = 0
        self.__min_bucket = self.__bucket
    
    def getBucketSize(self):
        return self.__bucket
    
    def load_factor(self):
        return self.__size / self.__bucket if self.__bucket else 0.0

    # hash function to map keys to bucket index
    def hashFunction(self, key):
        return (hash(key) % self.__bucket)

    def insert(self, node):
        # get the hash index of key
        index = self.hashFunction(node.key)
        newNode = self.__table[index].update(node)
        if newNode:
            self.__size += 1
            # Check load factor and rehash if necessary
            if self.load_factor() > self.maxinumLoadFactor:
                self.__rehash(self.__bucket * 2)

    def delete(self, key):
        index = self.hashFunction(key)
        if not self.__table[index].find(key):
            return
        hasDeleted = self.__table[index].delete(key)
        if hasDeleted:
            self.__size -= 1
            # Check load factor and rehash if necessary
            if (self.load_factor() < self.minimumLoadFactor and self.__bucket > self.__min_bucket):
                self.__rehash(self.__bucket // 2)
    
    def get(self, key):
        index = self.hashFunction(key)
        node = self.__table[index].find(key)
        if node is not None:
            return node.value
        else:
            return None
        
    def display(self):
        for i, ll in enumerate(self.__table):
            print(f"Bucket {i}: ", end="")
            for node in ll:
                print(f"({node.key}: {node.value}) -> ", end="")
            print("None")
        
    def __rehash(self, bucketSize):
        new_bucket = max(1, int(bucketSize))
        oldTable = self.__table

        self.__bucket = new_bucket
        self.__table = [LinkedList() for _ in range(self.__bucket)]

        for ll in oldTable:
            cur = ll.head
            while cur is not None:
                next = cur.next        
                cur.next = None       
                idx = self.hashFunction(cur.key)  
                cur.next = self.__table[idx].head
                self.__table[idx].head = cur
                cur = next
