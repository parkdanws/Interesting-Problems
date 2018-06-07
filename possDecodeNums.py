"""
June 6 2018

problem and some of solution based off Daily Coding Problem #7.
Commentary is mine, and notable changes made to code

given: mapping from each letter of alphabet to number (a = 1, b = 2... z = 26)
and a number, count the number of ways it can be decoded.
Assume: message is decodable

eg. 111: aaa, ak, ka -> 3
001: invalid input
"""

"""
seems like another dynamic programming problem.
given some integer, at each additional number
considered, it can be seen as a 'letter' on its own,
or a pair with the previous.
This question is about as straightforward a dp question can be. 

The solution is recursive, which makes a lot of sense. it
is better at detecting invalid solution

"""
def main():
    d = 111
    d2 = 1
    d3 = 1111
    print(possDecodeNums(d3))

def pdnsoln(message):
    """
    recursive given solution. basically similar as my solution except
    this doesn't explicitly keep a table, but rather the values
    are 'bubbled' up from end to beginning as the recursive calls
    return.
    """
    message = str(message)
    if message.startswith('0'):
        return 0
    elif message == "":
        return 1

    val = pdnsoln(s[1:])

    if int(message[:2]) <= 26:
        val += pdnsoln(s[2:])

    return val
    

def possDecodeNums(message):
    """
    my solution. is iterative
    """
    #assuming that message is an integer
    message = str(message)
    tab = set()
    for i in range(1,27):
        tab.add(str(i))

    # initializing dp is interesting
    # we are almost acknowledging that a double may exist
    dp = [1,1]

    for i in range(1,len(message)):
        val = dp[i]
        
        if message[i-1:i+1] in tab:
            val += dp[i-1] 
        dp.append(val)
    
    return(dp[-1])

if __name__ == "__main__":
    main()
