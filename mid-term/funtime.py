""" funtime.py | Sat, Mar 20, 2017 | Roman S. Collins

    A timeit like function for benchmarking Python programs.

"""
import time

def timeme(myfun):
    starttime = time.time()

    outp = myfun

    endtime = time.time()

    return outp, (endtime - starttime)

def main():
    """ Doctests:
        >>> outp = timeme("test")
        >>> isinstance(outp, tuple)
        True

        # Returns a tuple with output from a function
          and it's execution time
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
