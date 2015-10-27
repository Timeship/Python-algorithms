#!/usr/bin/env python
# coding=utf-8
'''顺序查找'''
def sequential_search(a_list,item):
    pos = 0
    found = False
    for pos,obj in enumerate(a_list):
        if a_list[pos] == item:
            found = True
    #return found
    for obx in range(len(a_list)): #py3里xrange和range合并
        if a_list[obx] == item:
            found = True
    return found
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    #return found

test_list = [1,2,32,5,8,17,19,42,13,0]
print(sequential_search(test_list,3))
print(sequential_search(test_list,13))

'''二分查找'''
def binary_search(a_list,item):
    first = 0
    last = len(a_list) -1
    found = False
    while first <= last and not found:
        midpoint = (first+last)//2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

test_list = [0,1,2,3,8,13,17,19,32,42]
print(binary_search(test_list,3))
print(binary_search(test_list,13))

'''哈希查找'''
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    #put data in slot
    def put_data_in_slot(self,key,data,slot):
        if self.slots[slot] == None:
            self.slots[slot] = key
            self.data[slot] = data
            return True
        else:
            if self.slots[slot] == key:
                self.data[slot] == data
                return True
            else:
                return False

    def put(self,key,data):
        slot = self.hash_function(key,self.size)
        result = self.put_data_in_slot(key,data,slot)
        while not result:
            slot = self.rehash(slot,self.size)
            result = self.put_data_in_slot(key,data,slot)

    def hash_function(self,key,size):
        return key%size

    def rehash(self,old_hash,size):
        return (old_hash+1)%size

    def get(self,key):
        start_slot = self.hash_function(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position,len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

if __name__=='__main__':
    table = HashTable()
    table[54] = 'cat'
    table[26] = 'dog'
    table[93] = 'lion'
    table[17] = 'tiger'
    table[77] = 'bird'
    table[44] = 'goat'
    table[55] = 'pig'
    table[20] = 'chicken'
    print(table.slots)
    print(table.data)
