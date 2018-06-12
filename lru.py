"""
June 12 2018

problem and solution based off Daily Coding Problem #52.
Commentary is mine, and notable changes made to code

Implement an LRU cache
initialized with cache size n

-set(key,value) method; if there are n items already
in cache, and this item is not already in cache, remove LRU item

-get(key): get value at key. if no key exists, return null

each op should run O(1)
"""

"""
the set/get and O(1) suggests the use of dictionary with extra bookkeeping
The ordering data structure sure feels like a queue.

problem is that we don't want to scan through queue when updating.
I'll use a doubly linked list

#partway note: this became a systems problem, not an algorithm one, with lots
of stress testing. I feel like I may have missed some sophisticated
answer, and am needlessly in the bogs.

My answer seems to work; it should run in O(1) because I don't 
scan anything. However, it is pretty ugly lol
"""

class LRU(object):
    def __init__(self,n):
        self.n = n
        self.currN = 0

        self.d = {}
        self.head = None
        self.tail = None

    def set(self,key,value):
        if self.currN == 0: #assuming self.n > 1
            b =  be(key)
            self.head = self.tail = b 
            self.d[key] = (value,b)
            self.currN += 1
            
        elif self.currN == self.n and key not in self.d:
            b =  be(key)
            del self.d[self.head.key]
            self.d[key] = (value,b)

            self.tail.post = b

            tmp = self.head
            self.head = self.head.post
            del tmp
            
            b.prev = self.tail
            self.tail = b
            self.head.prev = None

        elif self.currN == self.n and key in self.d:
            (v,n) = self.d[key]
            self.d[key] = (value,n)

            npr = n.prev
            npo = n.post

            if npr != None:
                npr.post = npo
            if npo != None:
                npo.prev = npr
            if n == self.head:
                self.head = npo

            if self.tail != n:
                self.tail.post, n.prev = n , self.tail
                self.tail = n

            n.post = None

        elif self.currN < self.n:
            b = be(key)
            self.tail.post, b.prev = b, self.tail
            self.tail = b
            self.d[key] = (value,b)
            self.currN += 1
            
    def get(key):
        return self.d.get(key,None)

    def printLL(self):
        curr = self.head
        while curr != None:
            print(curr)
            curr = curr.post
            
class be(object):
    def __init__(self,key,prev = None, post = None):
        self.key = key
        self.prev = prev
        self.post = post

    def __str__(self):
        return "val: {}; prev: {}; post: {}".format(self.key,repr(self.prev),repr(self.post))

    def __repr__(self):
        return "<LL node with value {}>".format(self.key)
