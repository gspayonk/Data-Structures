import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

#a new element is added at one end and an element is removed from that end only.
class Stack:
    def __init__(self):
        # self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    #adds to the front
    def push(self, value):
        self.storage.add_to_head(value)

    #removes and returns last value from the list or given index value
    def pop(self):
        return self.storage.remove_from_head()

    def len(self):
        return len(self.storage)
