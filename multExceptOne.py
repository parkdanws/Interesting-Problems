"""
Problem statement:
Given array
return new array so that each element at i of the new array
is the product of all the numbers in original array except the
one at location i.
"""
#simple solution
x = [1,2,3,4,5]

from functools import reduce

# a two liner!
allPdt = reduce(lambda i,j: i * j, x) # O(n)
ans = [allPdt/k for k in x] #O(n)
#O(n)

"""
Solution without using division
Idea: build a list of partial products of elements before
the current index, and those after
"""

prefix = [1, x[0]]
for i in x[1:-1]:
    prefix.append(prefix[-1]*i)

suffix = [x[-1],1]
for i in x[-2:0:-1]:
    suffix.insert(0,suffix[0]*i)

ret = []
for i in range(len(x)):
    ret.append(prefix[i]*suffix[i])
#O(n)
print (ret)
