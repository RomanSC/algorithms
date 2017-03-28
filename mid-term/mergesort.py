""" mergesort.py | Fri, Mar 20, 2017 | Roman S. Collins
    -------------------------------------------------------------

    An example of mergesort written in Python. Mergesort splits
    a list into pairs comparing each first element of a list
    with the next (merging in order) to determine which items
    go first.

    At the bottom of the recursion tree/stack mergesort compares
    two items individually, given the two items are each in a
    single item list. By comparing each first element the order
    of the element is determined. One step up in the tree two
    lists containing two items are compared using their first
    elements. List 1 element 1 is less than List 2 element 1
    therefore List 2 is placed after List 1.

    -------------------------------------------------------------

    Mergesort is O(n log n). ...unless you write it in Python.

    Then it's O(n) where n is the amount of times a CS student
    must implement basic data structures in a programming
    language too high level to benefit from them.

    When Python has sort().

    -------------------------------------------------------------

    Sources:
    - Python: MergeSort Algorithm (YouTube)
      https://www.youtube.com/watch?v=Nso25TkBsYI

    - Problem Solving with Data Structures and Algorithms:
      http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html

    - Mergesort (Wikipedia):
      https://en.wikipedia.org/wiki/Merge_sort

"""
from createlist import create
from funtime import timeme

def mergesort(mylist):
    if len(mylist) > 1:
        """
        "Recall that the slicing operator is O(k) where k is the
        size of the slice. In order to guarantee that mergeSort
        will be O(n log n) we will need to remove the slice operator.
        Again, this is possible if we simply pass the starting and
        ending indices along with the list when we make the recursive
        call. We leave this as an exercise."

        -- Problem Solving with Data Structures and Algorithms

        In wich case this mergesort algorithm should be O(n ** log n)
        without some implementation does not slice using the default
        Python list comprehension for each step.
        """
        # TODO
        # Address this issue
        mid = len(mylist)//2
        low = mylist[:mid]
        high = mylist[mid:]

        mergesort(low)
        mergesort(high)

        i, j, k = 0, 0, 0

        # Sorts lists for comparison
        while i < len(low) and j < len(high):
            if low[i] < high[j]:
                mylist[k] = low[i]
                i += 1
            else:
                mylist[k] = high[j]
                j += 1

            k += 1

        #print(mylist)

        # Compare items and move indeces
        while i < len(low):
            mylist[k] = low[i]
            i += 1
            k += 1

        #print(mylist)

        # Compare items and move indeces
        while j < len(high):
            mylist[k] = high[j]
            j += 1
            k += 1

        #print(mylist)

    else: # The list is already sorted
          # because it's length is one.
        return mylist

    return mylist

def main():
    mylist = create(iterations=200000, floor=1, ceiling=13, countby=3)
    #mylist = [7, 32, 4, 2, 1, 3]
    print("Unsorted   :", mylist)
    mergesorted, time = timeme(mergesort(mylist))
    print("Mergesort  :", mergesorted, time)
    #pythonsorted, time = timeme(sorted(mylist))
    #print("Pythonsort :", pythonsorted, time)


if __name__ == "__main__":
    main()
