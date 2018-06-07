"""
June 5 2018

problem and solution based off Daily Coding Problem #49.
Commentary is mine, and notable changes made to code

Given an array of numbers
Find max sum of any contiguous subarrays
Constraint: O(N)

eg: 
[33, -10000, 34, -1, 58] -> 34 + -2 + 58 = 90
[-1, -22, -333] -> 0 
"""


"""
A naive dynamic programming solution would be to make a 
NxN table where one side is starting index and the other
is the ending index.
This would work, and is simple but would run O(N^2)

We must be keeping a single running value somehow.

Insight: the only time we don't want to include values is
when they are negative. 

When we see a negative value, we have two options:
keep the values before the negative, or ignore these values
and see what kinds of values are after the negative.

Whether we keep or discard depends on whether the sum of the values
before the negative are greater than the negative value.
if so, we keep. ow, we discard.

We 'chunk' runs of numbers: positive or negative

if we find a negative chunk, we first see whether the preceding
positive chunk is larger than it. If not, than we are
better off ignoring think negative chunk entirely. We do this
by storing the previous positive chunk, and then skipping the 
negative chunk

if we see that the preceding positive chunk is larger than it,
then we have to consider whether including it and the next positive 
chunk is worth while. This is true if the next positive chunk
after the negative chunk is larger in magnitude than the negative 
chunk.
"""

def main():
    d =  [34, -50, 42, 14, -5, 86]
    d2 =  [-5, -1, -8, -9]
    print(solution(d))

def solution(data):
    """
    Solution: Even simpler than my solution. my fundamental intuition
    was correct; i have to be braver

    This algo is aka Kadane's algorithm. O(N) time, O(1) Space

    I hate it when the solution is ridiculously simple
    """
    max_atm = 0 #max at each step
    max_global = 0 #global max

    for d in data:
        max_atm = max(d,max_atm + d)
        max_global = max(max_global,max_atm)

    return max_global


def maxSASum(data):
    """
    My solution.
    runs O(N) (2*N max), O(N) space 
    """
    currind = 0
    currentchunk = 0    
    maxv = []

    while currind < len(data):
        ei = endInd(data,currind)
        candidate = run(data,currind,ei)#current chunk

        if candidate < 0:
            q = candidate #neg chunk
            #if prev chunk is not greater than this negative
            nei = endInd(data,ei)#next pos chunk end ind
            nc = run(data,ei,nei)#next positive chunk value

            if currentchunk + q < 0:
                maxv.append(currentchunk)
                currentchunk = nc
                currind = ei
                continue

            #not worth including pre-q chunk
            if nc + q < 0 :
                maxv.append(currentchunk)
                currind = nei
                currentchunk = nc

            else:
                currentchunk += q + nc
                currind = nei
                
        else:
            currentchunk = candidate
            currind = ei

    maxv.append(currentchunk)
    return max(maxv)

def run(data,st,end):
    ret = 0
    for i in range(st,end):
        ret += data[i]
    return ret

def endInd(data,st):
    if data[st] >= 0:
        switch = True
    else:
        switch = False
    i = st

    while (data[i] >= 0) == switch:
        i += 1
        if i > len(data)-1:
            break

    return i #goes one past
        
if __name__ == "__main__":
    main()
