"""
June 5 2018

problem and solution based off Daily Coding Problem #3.
Commentary is mine, and notable changes made to code

A node class is defined below.
Say that we create a binary tree using these nodes
Given a node root, find a way to transform it into a string.
This string must have the property (and make a method) to 
recreate the original binary tree from the tree alone.
"""
class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

"""
Given a simple tree,
  A
 / \
B   C

We can transform it into a string 
B N N A C N N 
where N represents the empty children of B and C.

We note, though that this becomes quickly problematic when we 
add more layers, and consider unbalanced trees. We can't find
the true root in this format.

Instead, we should store the tree above in the following fashion
A B N N C N N
where the first element is clearly the root.
see S-expressions in lisp
"""

#encode the tree to string recursively
def encode(root):
    """
    argument: node object
    returns: string of tree using node as root
    """
    if root == None:
        return "N"
    l = encode(root.left)
    r = encode(root.right)

    #see discussion above for string format
    return "%s %s %s"%(root.val, l, r) 

def decode(string):
    """
    argument: valid encoded string
    returns: root node of recreated binary tree
    """
    #iter object allows us to not worry about index location
    strList = iter(string.split(" "))

    def __dhelp():
        """
        used by decode
        recursively re-creates tree
        """
        #iterators are cool! 
        rootV = next(strList)

        #we've reached past leaf; don't create a new node. just return
        if rootV == "N":
            return None

        rootNode = Node(rootV)
        rootNode.left = __dhelp()
        rootNode.right = __dhelp()
        
        return rootNode

    return __dhelp()

# Code currently untested.
