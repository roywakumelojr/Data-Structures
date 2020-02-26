import sys
import os

sys.path.append('./doubly_linked_list') 
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    # def __init__(self, limit=10):
    #     self.limit = limit
    #     self.dict = {}
    #     self.storage = DoublyLinkedList()

    ## LECTURE SOLUTION
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = dict()
        self.order = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    # def get(self, key):

    #     if key in self.dict:
    #         item = self.dict[key]
    #         self.storage.move_to_front(item)
    #         return item.value[1]

    #     else:
    #         return None

    ## LECTURE SOLUTION
    def get(self, key):
        # If the key is in the storage
        if key in self.storage:
            # Move it to the end
            node = self.storage[key]
            self.order.move_to_end(node)

            # Return the value
            return node.value[1]

        #If not
        else:
            # Return None
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    
    # def set(self, key, value):

    #     if key in self.dict:
    #         self.storage.delete(self.dict[key])

    #     if self.limit  <= len(self.storage):
    #         item = self.storage.remove_from_tail()
    #         del self.dict[item[0]]
            
    #     self.storage.add_to_head((key, value))
    #     self.dict[key] = self.storage.head

    ## LECTURE SOLUTION

    # First Walk Through
    # def set(self, key, value):
        # if the cache is empty:
            # Add the key and value to the linkedlist
            # Add the key and value to the dictionary
            # Increment the size 
        # If the cache is empty:
            # Check and see if the key is in the dictionary
                # If it is
                    # overrite the value and move it to the end (Mostly changed side)
                    # move it to the emd
                # If it isn't 
                    # Check and see if the cache is full
                        # If cache is not full
                            # same as if cache is empty
                        # If cache is full
                            # Remove the oldest from the dictionary and linkedlist
                            # Reduce the size
                            # Same as if the cache is empty   
                            # 

    # Refactored Walk Through
    def set(self, key, value):
       
        # Check and see if the key is in the dictionary
        if key in self.storage:
            # If it is
            node = self.storage[key] ## Grabing the full node which contains the key
            # overrite the value and move it to the end (Mostly changed side)
            node.value = (key, value)
            # move it to the end
            self.order.move_to_end(node)
            # Return to exit the function
            return

           
        # Check and see if the cache is full
        if self.size >= self.limit:
            # If cache is full
            # Remove the oldest from the dictionary
            del self.storage[self.order.head.value[0]] 
            # Remove oldest from the linkedlist
            self.order.remove_from_head()
            # Reduce the size
            self.size -= 1

        # Add the key and value to the linkedlist
        self.order.add_to_tail((key, value))
        # Add the key and value to the dictionary
        self.storage[key] = self.order.tail
        # Increment the size
        self.size += 1        


########## NOTES ###############################
# Real use of LRU cache
# - Browser cacheing
# - API calls
# - Makes a product work better by increasing it's performance