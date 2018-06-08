"""
June 8 2018

problem and solution based off Daily Coding Problem #8.
Commentary is mine, and notable changes made to code

unival (universal value) tree is a tree where all nodes under it
have the same value.

Assuming that the root needs to be same as all others

Given root to binary tree
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
    print(univTree(root4)[0])

def univTree(root):
    if root == None:
        return(0,None,True)

    (ln,lv,ls) = univTree(root.left)
    (rn,rv,rs) = univTree(root.right)

    c = 0
    roots = False
    if lv == None:
        lv = root.value
    if rv == None:
        rv = root.value

    if ls == rs == True and lv == rv:
        c += 1
        if lv == rv == root.value:
            roots = True

        if lv == None or rv == None:
            roots = True

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
    rll = node(1)
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

if __name__ == "__main__":
    main()
