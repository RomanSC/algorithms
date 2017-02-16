""" singly.py | Fri, Feb 10, 2017 | Roman S. Collins

    Assignment:

    Implement and test a doubly-linked list in Python which
    can serve both as a stack and queue. Your API should include
    at least methods for __str__, push, pop, (i.e. the stack
    API), enqueue and dequeue (i.e. the queue API), reverse,
    nth (i.e. return the nth element of the list) and a way
    to insert a new element into the list.

    A DoublyLinkedList API in Python.

"""
from node import *

class DoublyLinkedList:
    def __init__(self, label='DoublyLinkedList'):
        self.label = label
        self.indx = - 1
        """
            List index starts at - 1
            so that dd.findx(0) returns
            the 0th item in the list,
            just like dd[0].

        """
        self.nth = Node(None)
        self.last = self.nth

    def __str__(self):
        return '{} {}'.format(self.label + ':', self.nth.data)

    def push(self, data):
        new_node = Node(data, lpointer = None, rpointer = self.nth)
        # TODO:
        # leftmost node rpointer points to rightmost
        # must have index function

        self.nth = new_node
        self.indx += 1
        print(self.nth.data)

    def pop(self):
        self.indx -= 1
        pass

    def queue(self):
        pass

    def enqueue(self):
        pass

    def findx(self, n):
        """
If self.indx even index left:
<-- lpointer.data <-- lpointer.lpointer.data

    self.indx = 2:
    *<-- {|2: lpointer.lpointer.lpointer.data |} -->

    self.indx = 1:
    *<-- {|1: lpointer.lpointer.data |} -->

    self.indx = 0:
    *<-- {|0: lpointer.data |} -->

If odd index right:

    self.indx = 0:
    <-- { 0|: lpointer.data |} -->*

    self.indx = 1:
    <-- { 1|: lpointer.lpointer.data |} -->*

    self.indx = 2:
    <-- { 2|: lpointer.lpointer.lpointer.data |} -->*

    """
        if (self.indx % 2) == 0: # Even
            indx = self.indx
            curr_node = self.nth

            if (n > self.indx):
                raise IndexError('list index out of range\nlist index out of range')
            else:
                indx = self.indx
                curr_node = self.nth

                while (indx > n):
                    print(indx)
                    current_node = curr_node.lpointer
                    indx -= 1

            print(current_node)
            #return current_node.data

        elif (self.indx % 1) == 0: # Odd
            pass

    def return_nth(self):
        return self.nth

    #def reverse(self):

def main():
    doubly = DoublyLinkedList()
    doubly.push('foo')
    doubly.push('baz')
    doubly.push('bar')

if __name__ == '__main__':
    main()

