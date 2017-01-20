""" maths.py | Thu, Jan 19, 2017 | Roman S. Collins

    Chapter 1 of Problem Solving with Algorithms and Data Structures

    Demonstrating creating a "Fraction" class in Python

"""
import doctest

class Fraction:
    """ The Fractions class as

        Fractions - Doctest:
        >>> (1 / 4) + (1 / 2)
        0.75
        >>> 3 / 4
        0.75
        >>> print(Fraction(1, 4))
        1/4
    """

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # Ha, implemented this before reading this section
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, plus):
        new_numerator = (self.numerator * plus.denominator) + (self.denominator * plus.numerator)
        new_denominator = (self.denominator * plus.denominator)

        common_denominator = self.get_common_denominator(new_numerator, new_denominator)

        return Fraction(new_numerator // common_denominator, new_denominator // common_denominator)

    def __eq__(self, compare):
        first_number = (self.numerator * compare.denominator)
        second_number = (compare.numerator * self.denominator)

        return first_number == second_number

    def get_common_denominator(self, fract_one, fract_two):
        """ Like the counting function but using the
            Fractions class in this program.

            "Is this one lower? OKAY this one is now
            that one. Is this one lower? OKAY this
            one is now that one. Is this one lower!?
            No. :( Okay, I'll stop..."

            Use floor division to store the fractions
            in lowest terms until they are closest to
            zero or zero but no less.

            i.e. Common denominators are found, then
            the two fractions are divided.

            Doctest:
            >>> (1 / 3) % (1 / 6)
            0.0
            >>> (1 / 32) % (7 / 42)
            0.03125
        """
        while fract_one % fract_two != 0:
            old_fract_one = fract_one
            old_fract_two = fract_two

            fract_one = old_fract_two
            fract_two = old_fract_one % old_fract_two

        return fract_two


class Sum:
    """ Summation - Doctest:
        >>> print(Sum(400, 1))
        400
    """

    def __init__(self, upper_bound, lower_bound):
        for self.lower_bound in range(upper_bound + 1):
            if self.lower_bound <= upper_bound:
                self.lower_bound =+ self.lower_bound

    def __str__(self):
        #TODO: Make string method more interesting
        return str(self.lower_bound)

#    def __int__(self):
#        #print(self.lower_bound)
#        return self.lower_bound

def main():
    fract1 = Fraction(1, 4)
    fract2 = Fraction(1, 2)
    fract3 = Fraction(1, 2)
    fract4 = Fraction(1, 2)


    print('Fraction: {}'.format(fract1), '+', fract2)
    print(fract1 + fract2, '\n')

    print('{} is equal to {}?: '.format(fract3, fract4))
    print(fract3 == fract4, '\n')

    #print(Sum('Sigma', 100, Fraction(1, (1 / 1 ** 2))))

    #print(Sum('Sigma', 100, Fraction(1, (1 / n ** 2) for n in range(100))))

    #for i in range(ub):
    #    #print(i)
    #    i = i ** 2
    #    n = Fraction(lb, i)
    #    total = Sum('Sigma', ub, n)
    #    #total = Sum('Sigma', ub, Fraction(lb, (1 / i ** 2)))
    #    #print(total)

    iterations = []

    for i in range(100 + 1):
        if i >= 1:
            n = (i ** 2)
            iteration = (1 / n)
            #iteration = Fraction(1, n)

        try:
            #print(iteration)
            iterations.append(iteration)
        except:
            if i == 0:
                iterations.append(i)
            # Except pass here, so that
            # if "function" is equal to
            # zero, UnboundLocalError
            # is not thrown and the
            # can proceed
            pass

    #print(len(iterations))
    print(sum(iterations))

    #Sum('Sigma', 100, function)

    #print(total)

if __name__ == '__main__':
    doctest.testmod()
    main()
