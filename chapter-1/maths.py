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

    """ Need Fraction() to be able to be interpreted as
        a float or integer if true...

        Python Documentation:
        https://docs.python.org/3/library/stdtypes.html

        Assumed my methods would be __int__, __float__
        which should return int() and float() objects
        respectively. But checked like this:

        >>> dir(float())
        ['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__',
        '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__',
        '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__',
        '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__',
        '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__',
        '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate',
        'fromhex', 'hex', 'imag', 'is_integer', 'real']

        >>> dir(int())
        ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__',
        '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
        '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__',
        '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__',
        '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__',
        '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__',
        '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
        '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag',
        'numerator', 'real', 'to_bytes']

        int() has no is_integer() method like this:
        >>> float(7.0).is_integer()
        True

        Stack Overflow - Checking whether a variable is an integer or not
        https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not#3501408
        >>> isinstance(7, int)
        True

        >>> isinstance(7.2, int)
        False

        >>> isinstance(7.2, float)
        True

        Must also understand the properties of integers or
        to understand when to return them or no...

    """
    def __int__(self):
        #if (self.numerator % self.denominator) == 0:
        #    return int(self.numerator / self.denominator)
        if isinstance((self.numerator / self.denominator), int):
            return int(self.numerator / self.denominator)


    def __float__(self):
        #if (self.numerator % self.denominator) != 0:
        #    print(self.numerator / self.denominator)
            #return self.numerator / self.denominator
        if isinstance((self.numerator / self.denominator), float):
            return float(self.numerator / self.denominator)


#class Sum:
#    """ Summation - Doctest:
#        >>> print(Sum(400, 1))
#        400
#    """
#
#    def __init__(self, upper_bound, lower_bound):
#        for self.lower_bound in range(upper_bound + 1):
#            if self.lower_bound <= upper_bound:
#                self.lower_bound =+ self.lower_bound
#
#    def __str__(self):
#        #TODO: Make string method more interesting
#        return str(self.lower_bound)
#
#class Sigma:
#    def __init__(self, upper_bound, lower_bound):
#        iterations = []
#        for lower_bound in range(upper_bound + 1):
#            if lower_bound >= 1:
#                n = (lower_bound ** 2)
#                #iteration = Fraction(1, n)
#                iteration = (1 / n)
#            try:
#                iterations.append(lower_bound)
#            except:
#                if lower_bound == 0:
#                    iterations.append(lower_bound)
#                else:
#                    pass
#
#        print(Sum(iterations))


def main():
    """
    fract1 = Fraction(1, 4)
    fract2 = Fraction(1, 2)
    fract3 = Fraction(1, 2)
    fract4 = Fraction(1, 2)


    #print('Fraction: {}'.format(fract1), '+', fract2)
    #print(fract1 + fract2, '\n')

    #print('{} is equal to {}?: '.format(fract3, fract4))
    #print(fract3 == fract4, '\n')

    iterations = []

    # This can be done without creating a class
    for i in range(100 + 1):
        if i >= 1:
            n = (i ** 2)
            iteration = (1 / n)

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

    print(sum(iterations))

    #print(float(Fraction(1, 3)))

    for i in range(1, 21):
        if isinstance(float(Fraction(1, i)), float):
            print(float(Fraction(1, i)))

    """

    ub = (100 + 1)
    lb = 1
    iterations = []

    for i in range(lb, ub):
        iteration = float(Fraction(lb, (i ** 2)))
        iterations.append(iteration)
        print(iteration)
    print(sum(iterations))

if __name__ == '__main__':
    doctest.testmod()
    main()
