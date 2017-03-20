""" mergesort.py | Fri, Mar 20, 2017 | Roman S. Collins
"""
from createlist import create
from funtime import timeme

def mergesort(mylist):
    if len(mylist) > 1:
        low = mylist[:len(mylist)//2]
        high = mylist[len(mylist)//2:]
        mid = len(mylist)//2

        print(low)
        print(high)
        print(mid)

def main():
    mylist = create(iterations=2, floor=1, ceiling=13, countby=3)
    print(mylist)

    mergesort(mylist)

if __name__ == "__main__":
    main()
