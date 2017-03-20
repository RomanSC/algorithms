""" quicksort.py | Fri, Mar 20, 2017 | Roman S. Collins

    An example of quicksort written in Python.

    Source:
    https://en.wikipedia.org/wiki/Quicksort#Algorithm

    Pseudo Code (As far as I can tell, kinda broken):

    algorithm quicksort(A, lo, hi) is
        if lo < hi then
            p := partition(A, lo, hi)
            quicksort(A, lo, p – 1)
            quicksort(A, p + 1, hi)

    algorithm partition(A, lo, hi) is
        pivot := A[hi]
        i := lo - 1
        for j := lo to hi - 1 do
            if A[j] ≤ pivot then
                i := i + 1
                swap A[i] with A[j]
        swap A[i+1] with A[hi]
        return i + 1

"""
from createlist import create
from funtime import timeme

def quicksort(mylist):
    low = []
    med = []
    high = []

    if len(mylist) > 1:
        pivot = (mylist[0]+mylist[(len(mylist)//2)]+mylist[(len(mylist)-1)])//3

        for i in range(len(mylist)):
            if mylist[i] < pivot:
                low.append(mylist[i])

            if mylist[i] == pivot:
                med.append(mylist[i])

            if mylist[i] > pivot:
                high.append(mylist[i])

        return quicksort(low)+med+quicksort(high)

    else:
        return mylist

def main():
    mylist = create(iterations=20000,
                    floor=1,
                    ceiling=100,
                    countby=2)

    mylist, time = timeme(quicksort(mylist))
    elements = len(mylist)
    print("RESULT: ", time, "for", elements, "elements.")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
