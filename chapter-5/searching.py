""" searching.py | Mon, Mar 06, 2017 | Roman S. Collins

    An example of binary and sqeuntial searching in Python.

    Read the sequential, binary, and hashing parts of the Searching chapter in the text. (We're doing sorting next, so continue on into that if time allows.)

"""
import random, termcolor

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
        # >>> find, mylist = 3, [1, 2, 3]
        # >>> binary(find, mylist)
        # True
        # >>> find, mylist = 4, [1, 2, 3]
        # >>> binary(find, mylist)
        # False

        Source:
        https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array

    """

    # mylist = list(mylist)

    # l = mylist[:(len(mylist)//2)]
    # r = mylist[(len(mylist)//2):]

    # print("DEBUG: searching {} for {}".format(mylist, find))
    # print(mylist)
    # print("DEBUG: l and r")
    # print(l)
    # print(r)
    # print("\n")

    # if l[-1:][0] != find: # Recurse until false
    #     if find < l[-1:][0]:
    #         binary(find, l)

    #     elif find > l[-1:][0]:
    #         binary(find, r)


    # F: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # L: [1, 2, 3, 4, 5]
    # R: [6, 7, 8, 9, 10]


    # F: [1, 2, 3, 4, 5]
    # L: [1, 2]
    # R: [3, 4, 5]


    # F: [3, 4, 5]
    # L: [3]
    # R: [4, 5]


    # F: [4, 5]
    # L: [4]
    # R: [5]


    # mylist = list(mylist)

    # lo = mylist[:(len(mylist)//2)]
    # hi = mylist[(len(mylist)//2):]

    # print(lo)
    # print(hi)

    # while len(mylist) > 0:
    #     if find < lo[-1:][0]:
    #         if find == lo[-1][0]:
    #             return True
    #         mylist = lo[:(len(mylist)//2)]
    #     if find < lo[-1:][0]:
    #         if find == lo[-1][0]:
    #             return True
    #         mylist = hi[:(len(mylist)//2)]

    # if len(mylist) == 1 and mylist[-1:][0] != find:
    #     return False
    left = 0
    right = (len(mylist) - 1)
    midpoint = ((len(mylist)//2)-1)

    print(mylist)
    print(left)
    print(right)
    print(midpoint)
    print("\n")
    print(mylist[left])
    print(mylist[right])
    print(mylist[midpoint])
    print("\n")

def main():
    #find, mylist = 4, [random.randint(1, 5000) for n in range(1, 11)]
    find, mylist = 34, [n for n in range(1, 11)]
    find, mylist = 4, [n for n in range(1, 11)]

    #print(sequential(find, mylist))
    print(binary(find, mylist))
    #print(find in mylist)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

