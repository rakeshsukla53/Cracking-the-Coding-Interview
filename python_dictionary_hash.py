__author__ = 'rakesh'


# Python dictionaries are implemented using hash tables. It is an array whose indexes are obtained using a
# hash function on the keys. The goal of a hash function is to distribute the keys evenly in the array.
# A good hash function minimizes the number of collisions e.g. different keys having the same hash. Python does not
# have this kind of hash function. Its most important hash functions (for strings and ints) are very regular
# in common cases:


#print map(hash, (0, 1, 2, 3, 4))  #it will print out [0, 1, 2, 3, 4]

#print map(hash, ('rakesh', 'bikash', 'ekansh'))

print hash('a') & 15   #either do by 7 or 15 but not any random number

print hash('b') & 15

print hash('c') & 15

print hash('d') & 15

print hash('e') & 15

print hash('f') & 15

#We could use a linked list to store the pairs having the same hash but it would increase the lookup time
# e.g. not O(1) anymore.

#Open addressing is a method of collision resolution where probing is used. In case of ‘z’,
# the slot index 3 is already used in the array so we need to probe for a different index to
# find one which is not already used. Adding a key/value
#pair might take more time because of the probing but the lookup will be O(1) and this is the desired behavior.

#you are still wondering how the key value pair is stored in dictionary so it is used by hash table.

#jab keys jaaanke hash function mein it will generate a value which is mapped to your value

#the whole algorithm is discussed heree

'''We want to add the following key/value pairs: {‘a': 1, ‘b': 2′, ‘z': 26, ‘y': 25, ‘c': 5, ‘x': 24}. This is what happens:

A dictionary structure is allocated with internal table size of 8.

    PyDict_SetItem: key = ‘a’, value = 1
        hash = hash(‘a’) = 12416037344
        insertdict
            lookdict_string
                slot index = hash & mask = 12416037344 & 7 = 0
                slot 0 is not used so return it
            init entry at index 0 with key, value and hash
            ma_used = 1, ma_fill = 1
    PyDict_SetItem: key = ‘b’, value = 2
        hash = hash(‘b’) = 12544037731
        insertdict
            lookdict_string
                slot index = hash & mask = 12544037731 & 7 = 3
                slot 3 is not used so return it
            init entry at index 3 with key, value and hash
            ma_used = 2, ma_fill = 2
    PyDict_SetItem: key = ‘z’, value = 26
        hash = hash(‘z’) = 15616046971
        insertdict
            lookdict_string
                slot index = hash & mask = 15616046971 & 7 = 3
                slot 3 is used so probe for a different slot: 5 is free
            init entry at index 5 with key, value and hash
            ma_used = 3, ma_fill = 3
    PyDict_SetItem: key = ‘y’, value = 25
        hash = hash(‘y’) = 15488046584
        insertdict
            lookdict_string
                slot index = hash & mask = 15488046584 & 7 = 0
                slot 0 is used so probe for a different slot: 1 is free
            init entry at index 1 with key, value and hash
            ma_used = 4, ma_fill = 4
    PyDict_SetItem: key = ‘c’, value = 3
        hash = hash(‘c’) = 12672038114
        insertdict
            lookdict_string
                slot index = hash & mask = 12672038114 & 7 = 2
                slot 2 is free so return it
            init entry at index 2 with key, value and hash
            ma_used = 5, ma_fill = 5
    PyDict_SetItem: key = ‘x’, value = 24
        hash = hash(‘x’) = 15360046201
        insertdict
            lookdict_string
                slot index = hash & mask = 15360046201 & 7 = 1
                slot 1 is used so probe for a different slot: 7 is free
            init entry at index 7 with key, value and hash
            ma_used = 6, ma_fill = 6
'''



#how we are making sure that the dictionary is keep getting bigger if we add more values

'''More memory is used to make sure the probing doesn’t take too long so inserting a new item is fast enough. Taking your example of inserting 1000 keys, the following will happen:
1- array starts with size 8.
2- when used slots == 6 (2/3 of capacity), size increased to 32
3- when used slots == 22 (2/3 of capacity), size increased to 128
4- when used slots == 86 (2/3 of capacity), size increased to 512
5- when used slots == 342 (2/3 of capacity), size increased to 2048
The array will be resized 4 times to accommodate 1000 items and at that time you will have 1048 free slots but this helps with sparseness which is key.
'''










