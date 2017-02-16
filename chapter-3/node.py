""" node.py | Wed, Feb 15, 2017 | Roman S. Collins

    Assignment:

    Implement and test a doubly-linked list in Python which
    can serve both as a stack and queue. Your API should include
    at least methods for __str__, push, pop, (i.e. the stack
    API), enqueue and dequeue (i.e. the queue API), reverse,
    nth (i.e. return the nth element of the list) and a way
    to insert a new element into the list.

"""
class Node:
    def __init__(self, data, lpointer = None, rpointer = None):
        self.data = data
        self.lpointer = lpointer
        self.rpointer = rpointer

def main():
    pass

if __name__ == '__main__':
    main()
