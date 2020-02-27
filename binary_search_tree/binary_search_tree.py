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
        # #### Insert Value ####
        # If there is no node at root
        if not BinarySearchTree(value):
            return None

        # Compare value to the root
        # If value is smaller :
        # look left if node, repeat steps
        elif value < self.value: 
            if not self.left: 
                self.left = BinarySearchTree(value)

            #  if no node: Make new one with this value
            else: 
                self.left.insert(value)

        # If value is greater or equal
        # Look right, if node repeat steps
        elif value >= self.value: 
            if not self.right: 
                self.right = BinarySearchTree(value)

            #  if no node: Make new one with this value
            else: 
                self.right.insert(value) 

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #### Find Value ####
        # If no node at root, return false
        if not BinarySearchTree(target):
            return False

        # Compare value to root
        elif self.value == target:
            return True

        # If smaller:
        #     go left: look at node there
        elif target < self.value: 
            if not self.left: 
                return False
            else: 
                return self.left.contains(target)

        # Is greater or ==:
        #     go right
        elif target >= self.value: 
            if not self.right: 
                return False
            else: 
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        #### Get Max ####
        # If no right child, return this value
        if not self.right: 
            return self.value

        # Otherwise, go right
        else: 
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)

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
