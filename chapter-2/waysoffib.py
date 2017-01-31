""" waysoffib.py | Thu, Jan 26, 2017 | Roman S. Collins

    Sources:
    - S1: Dylan Murphy - Python tutoring
      http://pastebin.com/89dxMK2L

    - S2: 5 ways for fibonacci
      https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/

"""
import sys
sys.setrecursionlimit(18000)

# Global declarations for
# generator
a, b = 0, 1

class WAYSOFFIB:
    def __init__(self):
        self.cata = {}

    def catalogued(self, n):
        if (n == 0) or (n == 1):
            return n

        if n in self.cata:
            return self.cata[n]

        return self.catalogued(n - 1) + self.catalogued(n - 2)

        # TypeError: can only concatenate tuple (not "int") to tuple
        # return self.cata[n], self.cata
        # Tried to make this code return the dict
        # many ways but taking too long to debug
        # (Not because I tried returning after a return statement,
        #  I know that return exits a function/loop)
        #self.cata = self.catalogued(n - 1) + self.catalogued(n - 2)
        #return self.cata

    def not_catalogued(self, n):
        if (n == 0) or (n == 1):
            return n

        return self.catalogued(n - 1) + self.catalogued(n - 2)

    def looping(self, n):
        a, b = 1, 1

        for i in range(n - 1):
            a, b = b, a + b

        return a

    def generator(self):
        global a, b
        while True:
            a, b = b, a + b

        # pause the loop for later
        # while global a, b
        # become equal to the last
        # and second to last
        # n in the sequence
            yield a

    def gen(self, n):
        generate = self.generator()

        for i in range(n - 1):
            next(generate)
        return b

# Seems very similar to catalogued method?
class Memoize:
    def __init__(self, n):
        self.n = n
        # track
        self.memo = {}

    def __call__(self, arg):
        # it seems fib(n) is passed through the call method
        # ran out of time to fully test and learn about memoization
        # but going to do some reading after submitting this assignment
        if arg not in self.memo:
            self.memo[arg] = self.n(arg)
        return self.memo[arg]

def main():
    """ Doctest:
    >>> doctest_n = 5
    >>> doctest_waysoffib = WAYSOFFIB()
    >>> print(doctest_waysoffib.catalogued(doctest_n))
    5
    >>> print(doctest_waysoffib.not_catalogued(doctest_n))
    5
    >>> print(doctest_waysoffib.looping(doctest_n))
    5

    Not sure how to doctest memoization method
    googling was not succesful, but has been
    fully tested:

    #>>> doctest_memsoffib = Memoize(doctest_n)
    #>>> @Memoize
    #... doctest_memsoffib.gen(doctest_n))
    #5
    """

    """
    n = 5
    waysoffib = WAYSOFFIB()
    memsoffib = Memoize(n)

    print(waysoffib.catalogued(n))
    print(waysoffib.not_catalogued(n))
    print(waysoffib.looping(n))
    print(waysoffib.gen(n))
    """

    """
    #TODO: MEMOIZE
    @Memoize
    def fib(n):
        y, z = 1, 1
        for _ in range(n - 1):
            y, z = z , y + z
        return y

    print(fib(n))
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
