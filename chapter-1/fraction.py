""" fraction.py | Thu, Jan 19, 2017 | Roman S. Collins

    Chapter 1 of Problem Solving with Algorithms and Data Structures

    Demonstrating creating a "Fraction" class in Python

"""
import doctest

class Fraction:
    def __init__(self, title, numerator, denominator):
        self.title = title
        self.numerator = numerator
        self.denominator = denominator

    # Ha, implemented this before reading this section
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, plus):
        new_numerator = (self.numerator * plus.denominator) + (self.denominator * plus.numerator)
        new_denominator = (self.denominator * plus.denominator)

        common_denominator = gcd(new_numerator, new_denominator)

        return Fraction('Fraction', new_numerator // common_denominator, new_denominator // common_denominator)

    def __eq__(self, compare):
        pass
        first_number = (self.numerator * compare.denominator)
        second_number = (compare.numerator * self.denominator)

        return first_number == second_number

def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn

    return n

    #print(gcd(20,32))

def main():
    """ Doctest:
    >>> (1 / 4) + (1 / 2)
    0.75
    >>> 3 / 4
    0.75
    """

    fract1 = Fraction('Fraction', 1, 4)
    fract2 = Fraction('Fraction', 1, 2)
    fract3 = Fraction('Fraction', 1, 2)
    fract4 = Fraction('Fraction', 1, 2)


    print('Fraction: {}'.format(fract1), '+', fract2)
    print(fract1 + fract2, '\n')

    print('{} is equal to {}?: '.format(fract3, fract4))
    print(fract3 == fract4, '\n')

if __name__ == '__main__':
    doctest.testmod()
    main()
