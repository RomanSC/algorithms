""" doubly.py | Fri, Feb 10, 2017 | Roman S. Collins

    Assignment:

    Implement and test a doubly-linked list in Python which
    can serve both as a stack and queue. Your API should include
    at least methods for __str__, push, pop, (i.e. the stack
    API), enqueue and dequeue (i.e. the queue API), reverse,
    nth (i.e. return the nth element of the list) and a way
    to insert a new element into the list.

"""
class Node:
    """ Slots create faster access to class attributes
        where not dict is used, and can't be used.

        Since we are essentially implementing our
        own list API, and want to keep builtin
        Python functions like list and dicts
        to a minimum. So... why not.

        Sources:
        https://stackoverflow.com/questions/472000/usage-of-slots
    """
    __slot__ = 'data', 'prev_node', 'next_node'

    # This is all we need for our Node object
    def __init__(self, data, prev_node = None, next_node = None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

        # Instead of creating Node with a __str__
        # method, as that was giving me recursion
        # errors, clearly because as soon as
        # __str__ method is called, another
        # Node is called along with it's own
        # __str__ method, which calls the
        # previous Node into infinity

"""
    def return_prev(self):
        return self.prev_node

    def return_next(self):
        return self.next_node

    def new_prev(self, new_prev_node = None):
        self.prev_node = new_prev_node

    def new_next(self, new_next_node = None):
        self.next_node = new_next_node

    def new_data(self, new_data = None):
        self.data = new_data
"""
from termcolor import colored

#TODO
class DoublyLinkedList:
    """ "When inheriting from a class without __slots__, the __dict__ attribute of that class
        will always be accessible, so a __slots__ definition in the subclass is meaningless."

        From Stack Overflow discussion earlier
    """
    __slot__ = 'self.label', 'self.index', 'self.front_id', 'self.end_id'

    def __init__(self, label=''):
        self.label = label
        self.index = 0
        self.front_id = Node(None)
        self.end_id = Node(None)
        self.front_id.next_node = self.end_id
        self.end_id.prev_node = self.front_id

    def __str__(self, index=None):
        if index is None:
            # How to literally put {} into a string {{ and }}
            # https://stackoverflow.com/questions/5466451/how-can-i-print-literal-curly-brace-characters-in-python-string-and-also-use-fo
            return '<- {{{} | {} | {}}} ->'.format(self.front_id, self.front_id.data, self.end_id)
        #TODO:
        # Related to API for indexing over the list
        # For instance, Python default lists
        else:
            pass

    # Like isEmpty() from the chapter
    def empty(self):
        if self.front_id.data == None:
            return True
        elif self.front_id_data == None:
            return False

    #TODO:
    # Push should add to the front(top) as in a stack
    # first element
    def push(self, data=None):
        print('DEBUG: push() initiated')

    #TODO:
    # Pop should remove from the front(top) as in a stack
    # first element
    def pop(self):
        pass

    #TODO:
    # http://interactivepython.org/runestone/static/pythonds/BasicDS/WhatIsaQueue.html
    # rear | front
    # Queue should add to the "rear" as in a queue
    # first element
    def enqueue(self):
        pass
    #TODO:
    # Dequeue should remove from the "front" as in a queue
    # nth element
    def dequeue(self):
        pass

def main():
    doubly = DoublyLinkedList()
    print(doubly)
    print(doubly.empty())

    doubly.push(data='dog')
    print(doubly)

if __name__ == '__main__':
    main()
