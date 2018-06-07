"""
June 6 2018

problem and solution based off Daily Coding Problem #50.
Commentary is mine, and notable changes made to code

Given root to binary tree where leaves are numbers and internal nodes 
are arithmetic operator
evaluate it

eg.

    *
  /   \
 +     +
/  \  /  \
3  2  4  5

would evaluate (3+2)*(4+5)
"""

"""
This seems like a very simple problem of recursion.
Assuming that the input is some node class with
value, left and right pointers
where value stores the operator for internal nodes and a number
for leaf nodes; all as string form
"""

def binTreeOp(root):
    if root.leaf == True:
        return root.value
    return str(eval("{} {} {}".format(binTreeOp(root.left) +
                                      self.value +
                                      binTreeOp(root.right))))

                                      
                    
