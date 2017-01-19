""" sigma-s-summation.py | UTF-8 | Wed, Jan 18, 2017 | Roman S. Collins

∑ is the greek equivalent for "S"

"In mathematics, summation (capital Greek sigma symbol: ∑) is the
addition of a sequence of numbers; the result is their sum or total."
https://en.wikipedia.org/wiki/Summation

Khan Academy - Sigma notation:
https://www.youtube.com/watch?v=5jwXThH6fg4

YouTube - Not More Math for Dummies 1.1: Sigma Notation:
https://www.youtube.com/watch?v=5jwXThH6fg4

Wolfram Alpha:
https://www.wolframalpha.com/input/?i=sigma+100&rawformassumption=%7B%22F%22,+%22Sum%22,+%22sumfunction%22%7D+-%3E%221+%2F+n%5E2%22&rawformassumption=%7B%22F%22,+%22Sum%22,+%22sumvariable%22%7D+-%3E%22n%22&rawformassumption=%7B%22F%22,+%22Sum%22,+%22sumlowerlimit%22%7D+-%3E%221%22&rawformassumption=%7B%22C%22,+%22sigma%22%7D+-%3E+%7B%22SumWord%22%7D

Sigma 100 can be written like so:

    100
    ∑
    n = 1

Another way to write the example problem:

                   100
(1 / n ** 2 ) * (  ∑      )
                   n = 1

Where n is the lower limit.

One could try the built in sum() function, but it does not work with floats.

So I made my own.

Since naming my function "sum" is a bad idea:
http://www.dictionary.com/browse/tot?s=t

"""
import math, doctest

class Greek:
    def __init__(self, title=''):
        self.title = title

    def __str__(self):
        return self.title

    def tot(self, upper_limit, lower_limit):
        for lower_limit in range(upper_limit + 1):
            if lower_limit <= upper_limit:
                lower_limit =+ lower_limit
                #total = lower_limit
        return lower_limit

def main():
    """ Doctest:
    >>> n = 1
    >>> 1 / (n ** 2)
    1.0
    """
    n = 1
    G = Greek()
    total = G.tot(100, n)

    #print(total)

    print((1 / (n ** 2) * total))

    """ tot - Doctest:
    >>> print(G.tot(200, n)
    200
    """

if __name__ == '__main__':
    doctest.testmod()
    main()
