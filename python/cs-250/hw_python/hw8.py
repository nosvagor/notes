
# Today, we're going to work with trees.
# First we need to define a tree in python

class tree():
    def __init__(self, x, left, right):
        self.x = x
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left == None

    
    def __repr__(self):
        if self.isLeaf():
            return repr(self.x)
        else:
            return "[." + repr(self.x) + " " + repr(self.left) + " " + repr(self.right) + " ]"

    def __str__(self):
        return "\\Tree" + repr(self)

def leaf(x):
    return tree(x,None,None)

def branch(x,l,r):
    return tree(x,l,r)

# We can construct a tree with the branch and leaf constructors just like we did in class.
# I've implemented the repr() and str() functions that print out the tree
# using the qtree syntax from latex.
# Just use print(str(t)) to print the latex code to display the tree.

# Question 1
# construct the following trees.

#        1
#       / \
#      2   3
t1 = None


#        1
#       / \
#      2   3
#     / \
#    4   5
#       / \
#      6   7
t2 = None

#        1
#       / \
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7
t3 = None

# Question 2
# implement mirror from class.
# it should return a new tree, it shouldn't modify the current tree.
def mirrer(t):


# Question 3
# The weight of a path is the sum of all of the nodes in the path.
# for example, in the tree
#        1
#       / \
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7
# the path on the right (1,3,7) has weight 11.
# 
# write a function to return the maximum path weight.
# I don't care what path gave the weight, I just want the number.
# so, maxWeight(t3) should return 11
return maxWeight(t):
    return -1

# question 4:
# write a function the returns a tuple (bst,max)
# where bst is True if the tree is a binary search tree, and Falst otherwise.
# and max is the maximum number in the tree.
#
# example:
#        1
#       / \
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7
# should return (False, 7)
#        4
#       / \
#      /   \
#     2     6
#    / \   / \
#   1   3 5   7
# should return (True, 7)
def isBST(t):
    return (False, 0)

