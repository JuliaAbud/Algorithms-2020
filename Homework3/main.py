from ht import hashTable

if __name__ == "__main__":
    print("====================================")
    HObject = hashTable()
    HObject.insertKey(10)
    HObject.insertKey(10)
    HObject.insertKey(50)
    HObject.insertKey(100)
    HObject.insertKey(257)
    HObject.insertKey(10)
    HObject.insertKey(10)
    HObject.insertKey(50)
    HObject.insertKey(100)
    HObject.insertKey(257)
    HObject.insertKey(15)
    
    HObject.printHashTable()

    HObject.findKey(257)
    HObject.deleteKey(10)
    HObject.deleteKey(15)

    HObject.printHashTable()


