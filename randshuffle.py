"""
June 8 2018

problem and solution based off Daily Coding Problem #51.
Commentary is mine, and notable changes made to code

Given a random number generator that takes 'k' and returns a value 
between 1 - k (inclusive)
write a fn that shuffles a deck of 52 cards. The deck is 
represented as an array; shuffling should be performed only using
swaps.
Must run O(N)
Each of the 52! permutations must be equally likely
"""


"""
This one's hard. It's pretty unrelated to the formats that I am 
comfortable with

I don't know whether I am giving the k or not. 
If I can provide whatever k I want, the solution is pretty simple
"""
import random

def main():
    random.seed(a=50)
    deck = [i for i in range(1,53)]
    print (deck)
    shuffler(deck)
    print (deck)

def shuffler(deck):
    for i in range(len(deck)):
        j = randNumK(51)
        deck[i], deck[j] = deck[j],deck[i]

def randNumK(k):
    return random.randrange(1,k+1)

if __name__ == "__main__":
    main()
