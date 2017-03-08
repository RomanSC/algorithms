""" searching.py | Mon, Mar 06, 2017 | Roman S. Collins

    An example of binary and sqeuntial searching in Python.

    Read the sequential, binary, and hashing parts of the Searching chapter in the text. (We're doing sorting next, so continue on into that if time allows.)

"""
import random

def sequential(find, mylist):
    """ Doctest:
        >>> find, mylist = 3, [1, 2, 3]
        >>> sequential(find, mylist)
        True
        >>> find, mylist = 4, [1, 2, 3]
        >>> sequential(find, mylist)
        False
    """
    for item in mylist:
        if item == find:
            return True

    return False

def binary(find, mylist):
    """ Doctest:
        >>> find, mylist = 3, [1, 2, 3]
        >>> binary(find, mylist)
        True
        >>> find, mylist = 4, [1, 2, 3]
        >>> binary(find, mylist)
        False

        Source:
        https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array

    """
    mylist = list(mylist)

    l = mylist[:(len(mylist)//2)]
    r = mylist[(len(mylist)//2):]

    print("DEBUG: searching {} for {}".format(mylist, find))
    print(mylist)
    print("DEBUG: l and r")
    print(l)
    print(r)
    print("\n")

    if l[-1:][0] != find: # Recurse until false
        if find < l[-1:][0]:
            binary(find, l)

        elif find > l[-1:][0]:
            binary(find, r)

    return True

def main():
    #find, mylist = 4, [random.randint(1, 5000) for n in range(1, 11)]
    #find, mylist = 34, [n for n in range(1, 11)]
    find, mylist = 4, [n for n in range(1, 11)]

    #print(sequential(find, mylist))
    print(binary(find, mylist))
    #print(find in mylist)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

