""" createlist.py | Fri, Mar 20, 2017 | Roman S. Collins
"""
from random import shuffle

def create(iterations=100, floor=2, ceiling=10, countby=2, random=False):
    mylist = []

    if ceiling <= countby:
        mylist = "Don't use ceiling lower than countby!"

    for i in range(iterations + 1):
        for n in range(floor, ceiling, countby):
            mylist.append(n)

    if random:
        mylist = list(mylist)
        shuffle(mylist)

    return mylist

def main():
    """ Doctest:
        >>> a = create(iterations=2, floor=1, ceiling=10, countby=2, random=False)
        >>> b = create(iterations=2, floor=1, ceiling=10, countby=2, random=False)
        >>> print(a == b)
        True

        >>> a = create(iterations=2, floor=1, ceiling=10, countby=2, random=True)
        >>> b = create(iterations=2, floor=1, ceiling=10, countby=2, random=True)
        >>> print(a == b)
        False
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
