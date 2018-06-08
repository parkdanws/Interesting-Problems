"""
June 8 2018

problem and solution based off Daily Coding Problem #8.
Commentary is mine, and notable changes made to code

unival (universal value) tree is a tree where all nodes under it
have the same value.

Assuming that the 'tree' has to be at least 2 nodes
Assuming that the root needs to be same as all others

##first one is wrong

Given root to binary tree
"""

"""
for univTreeBad: I dun goof'd and misunderstood the question.
see next text chunk. the following rea

Recursive, obviously
Each root sends each child its own value
at leaf level, if the leaf value is same as parent's return 1.
at internal node, if self value is same as parent's, return 
the sum of the values from its two children plus 1 if the internal 
node's value is equivalent to the parent's. 0 o/w

The above intuition gets me pretty far, but it will ignore 
cases where both left and right children match the root; it will 
return two trees when there are actually 3. 

I have each node returning a tupule value so that a root can
account for this information
"""

"""
Here is attempt 2. 
"""
def main():
    root1 = input1()
    root2 = input2()
    root3 = input3()
    root4 = input4()
    root5 = input5()
    print(univTree(root5)[0])

def univTree(root):
    if root == None:
        return(0,None,True)
    # print ("current value: {}".format(root.value))

    (ln,lv,ls) = univTree(root.left)
    (rn,rv,rs) = univTree(root.right)

    if lv == None:
        lv = root.value
    if rv == None:
        rv = root.value

    c = 0
    roots = False
    
    if ls == rs == True and lv == rv:
        c += 1
        if lv == rv == root.value:
            roots = True
    
    # print ("-lnum, lval, lstatus: {} {} {}".format(ln,lv,ls))
    # print ("-rnum, rvar, rstatus: {} {} {}".format(rn,rv,rs))
    # print ("returning: {} {} {}".format(c + ln + rn,root.value, roots))
    return (c + ln + rn, root.value, roots)

def input5():
    a = 'a'
    b = 'b'
    c = 'c'

    rrr = node(b)

    rr = node(b,left = None,right = rrr)
    rl = node(b)

    r = node(b,rl,rr)
    l = node(c)

    return node(a,l,r)

def input4():
    a = 'a'
    A = 'A'

    rrr = node(A)

    rr = node(a,left = None, right=rrr)
    rl = node(a)

    r = node(a, rl,rr)
    l = node(a)

    return node(a,l,r)

def input3():
    l = node(0)
    r = node(1)
    return node(0,l,r)

def input2():
    return node(1)

def input1():
    rl = node(1)
    rlr = node(1)

    rl2 = node(1,rll,rlr)
    rr2 = node(0)

    r1 = node(0,rl2,rr2)
    l1 = node(1)

    root = node(0,l1,r1)
    return root    
    
class node(object):
    def __init__(self,val,left=None,right=None):
        self.value = val
        self.left = left
        self.right = right

def univTreeBad(root,pval):
    
    if root == None:
        return ("NO",0)
    
    c = 0
    if pval == root.value:
        c = 1

    print("In univTree. myval: {}, pval: {}".format(root.value,pval))
    (lv,cl) = univTree(root.left,root.value)
    (rv,cr) = univTree(root.right,root.value)

    if root.value == lv ==rv:
        c += 1
    
    print("--c, left, right: {}, {}, {}".format(c,cl,cr))
    return (root.value,c + cl + cr)

if __name__ == "__main__":
    main()
