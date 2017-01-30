""" execution-time.py | Mon, Jan 30, 2017 | Roman S. Collins

Demonstrating how to calculate execution time using a function
in Python...

Jim's example:

def run_time(f, n, loopcount=1000):
    # Return the run time in seconds of f(n)
    # see https://docs.python.org/2/library/time.html
    from time import time
    start = time()
    for loop in range(loopcount):
        anwer = f(n)
    end = time()
    return (end - start)/loopcount

Assumes a specific function is called within the loop.

Whereas attempt to make my loop "function agnostic",
ultimately not that different though

"""

from doctest import testmod
from time import time

def execution_time(some_function, iter_count):
    start_time = time()

    for iterations in range(iter_count):
        result = some_function

    end_time = time()

    exec_time = (end_time - start_time) / iter_count

    return result, exec_time

def main():
    """ Doctest:
    >>> print('Hello world!')
    Hello world!
    """

    sus = [1, 3, 34, 53, 645, 234, 6234, 111, 1123, 100, 12, 12, 23]

    result, exec_time = execution_time(sum(sus), 2000000)

    print('TEST: print \"result\", \"exec_time\":', result, exec_time)

if __name__=='__main__':
    testmod()
    main()
