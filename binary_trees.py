#####  binary_trees.py  #####

class Node: # This is the Class Node with constructor that contains data variable to type data and left,right pointers.
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive function to determine the length of tree along its longest path
def tree_length(tree):
    if tree is None:
        return 0
    if tree is not None:
        left_tree_length = tree_length(tree.left)
        right_tree_length = tree_length(tree.right)
        if right_tree_length > left_tree_length:
            return right_tree_length + 1
        else:
            return left_tree_length + 1
    else:
        return print("Possible Type Error; Sure You Gave Me A Tree?")

# Recursive function to determine if binary tree is or is not full?
def fullness(tree):    
    if tree is None:
        return True
    if (tree.left is None) and (tree.right is None):
        return True
    if (tree.left is not None) and (tree.right is not None):
        return (fullness(tree.right) and fullness(tree.left))
    else:
        return False

