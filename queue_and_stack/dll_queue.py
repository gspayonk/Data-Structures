import sys
sys.path.append('../doubly_linked_list') 
from doubly_linked_list import DoublyLinkedList

# import unittest
# from doubly_linked_list.doubly_linked_list import ListNode
# from doubly_linked_list.doubly_linked_list import DoublyLinkedList


#the least recently added item is removed first
class Queue:
    def __init__(self):
        # self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    #adds element to a queue
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        # self.size += 1

    #remove element from queue
    def dequeue(self):
        return self.storage.remove_from_head()
        # if value: self.size -= 1
        # return value
    
    #measures the length of the queue
    def len(self):
        # return self.size
        return len(self.storage)