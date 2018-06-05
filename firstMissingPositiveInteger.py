"""
June 5 2018

problem and solution based off Daily Coding Problem #4.
Commentary is mine, and notable changes made to code

Given: array of integers
Find: the first missing positive integer
Constraints: Constant space (no more than given list); O(N) runtime
Notes: Duplicates and negative values are allowed
EG:
[0,1,2,3] -> 4
[5,2,-59,1] -> 3
"""

"""
Solution:
We note that sorting would be the most intuitive solution; however
the best algorithms we have run O(N log(N)). We have to loosen 
some constraints.

We could try making a set() of values, but this violates the 
constant space requirement

The intuition is this: The value we want is going to be constrained
by len(inputList) + 1. 

We can use this property to loosen sorting property to only values
that are less than len(inputList) + 1.
"""

def firstMissingPositiveInteger(data):
    if not data:
        return 1

    #for each bucket index
    for i in range(len(data))
        #while bucket index and value isn't equal
        #AND while bucket value is within the range of valid values
        while i + 1 != data[i] and 0 < data[i] <= len(data):
            #grab bucket value at index i
            considered = data[i]
            #swap values at INDEX EQUAL TO BUCKET VALUE and current index
            data[i] , data[considered -1] = data[considered -1], data[i]

            #if we see that the two values are equal, quit
            if data[i] == data[considered-1]:
                break
        # result of this while loop is that at bucket index i,
        #we will either have the matching value or a value that
        #exceeds the range of valid values.

    #result of this for loop is that every index will either have
    #the correct bucket index to the degree it is possible

    #now find the first missing positive integer
    #second argument of enumerate is the starting number; we still
    #will consider every bucket in data
    for i, num in enumerate(data,1):
        if i != num:
            return i

    return len(data) + 1
        
"""
Example run:
The "for" loop index is bracketed

[3] 4 -1 1
[-1] 4 3 1
-1 [4] 3 1
-1 [1] 3 4
1 [-1] 3 4
1 -1 [3] 4
1 -1 3 [4]

notes: I like this problem a lot!
"""
