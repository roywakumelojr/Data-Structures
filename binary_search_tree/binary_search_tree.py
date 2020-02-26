import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        """
        #### Insert Value ####
        If there is no node at root 
        Compare value to the root
        If value is smaller :
            look left if node, repeat steps
            if no node: Make new one with this value
        If value is greater or equal
            Look right, if node repeat steps
            if no node: make new one with this value
        """
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        """
        #### Find Value ####
        If no node at root, return false
        Compare value to root
        If smaller:
            go left: look at node there
        Is greater or ==:
            go right
        """
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        """
        #### Get Max ####
        If no right child, return this value
        Otherwise, go right
        """
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
