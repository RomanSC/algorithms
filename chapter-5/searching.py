""" searching.py | Tue, Mar 07, 2017 | Roman S. Collins
"""
import random

def sequential(find, mylist):
    for item in mylist:
        if item == find:
            return True
    return False

def binary(find, mylist):
    pass
    for item in range(len(mylist)):
        if

def main():
    mylist = [random.randint(1, 5000) for n in range(1000000)]
    find = 135799

    print(sequential(find, mylist))
    print(find in mylist)

if __name__ == '__main__':
    main()

