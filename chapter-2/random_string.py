""" random_string.py | Wed, Feb 01, 2017 | Roman S. Collins

    Demonstrating returning random strings in Python.

"""
import random

class randStr:
    def rand_string(self, n):
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                    'w', 'x', 'y', 'z', ' ']
        abc_copy = list(abc[x] for x in range(len(abc)))
        return ''.join(random.sample(abc_copy, n))

def main():
    """ Again only sanity checks, because output of the
        function changes.

        Doctest:
        >>> len(randStr().rand_string(10))
        10
        >>> isinstance(randStr().rand_string(10), str)
        True
    """
    # Fill main with something other than pass
    print(randStr().rand_string(10))


if __name__=='__main__':
    main()
