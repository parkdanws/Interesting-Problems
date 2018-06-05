"""
June 5 2018

problem and solution based off Daily Coding Problem #5.
Commentary is mine, and notable changes made to code

cons(a,b): constructs a pair
car(pair): returns first element of pair
cdr(pair): returns last element of pair

cons is implemented as below.
implement car and cdr
"""
def cons(a,b):
    def pair(f): #pass in a function?
        return f(a,b) #what the hell
    return pair#returns a function

"""
APPARENTLY
there is something called a closure in computer programming
https://en.wikipedia.org/wiki/Closure_(computer_programming)

and that is what is holding data.
because pair() is defined within cons, it has access to the
a and b parameters given to cons() AKA a,b are within the lexical
scope of cons.

When cons() returns the pair() function, the knowledge of parameters
are retained. 

So cons returns an 'anonymous' function (pair)
This anonymous function itself takes in 'f' as parameter. the 'f' 
function is then called with a and b as its own parameters
We're looking at functions 3 levels deep lol

SO
car and cdr have to provide the 'pair' function with a function as 
a parameter. This function will be called with the data stored
within 'pair' function

what the hell indeed
"""
def car(pair):
    return pair((lambda a,b: a))

def cdr(pair):
    return pair((lambda a,b: b))


"""
PS: the example of closure in the wiki page is also really fun, and is
reproduced here
"""
def add(x):
    def addX(y):
        return y + x
    return addX #return a closure

def addD(x):
    return lambda y: x + y #returns a closure

#closures stored within variables
add1 = add(1)
add5 = add(5)
add9 = addD(9)

assert add1(3) == 4 ,"Something went wrong"
assert add5(3) == 8 ,"Something went wrong"
assert add9(3) == 12,"Something went wrong" 

#very very cool
