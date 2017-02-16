""" singly.py | Fri, Feb 10, 2017 | Roman S. Collins

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
        # Node objects should contain data
        # then each pointer, I chose the
        # Naming scheme "left" pointer
        # "right" pointer
        self.lpointer = lpointer
        self.rpointer = rpointer

class SinglyLinkedList:
    def __init__(self, label='SinglyLinkedList'):
        self.label = label
        self.indx = - 1 # overall amount of items in the list
        self.nth = Node(None) # first node in the list

    def __str__(self):
        return '{} {}'.format(self.label + ':', self.nth.data)

    def push(self, data):
        # How to: add operation
        # https://youtu.be/Ast5sKQXxEU?t=96
        new_node = Node(data, rpointer = self.nth)
        self.nth = new_node
        self.indx += 1

    def pop(self):
        # Swapparoo and -1 from indx
        self.nth = self.nth.rpointer # last item is always here
        self.indx -= 1

    def length(self):
        return (self.indx + 1)

    def findx(self, n):
        if n > self.indx:
            raise IndexError('list index out of range\nlist index out of range')
        else:
            indx = self.indx
            curr_node = self.nth
            while (indx != n):
                curr_node = curr_node.rpointer
                indx -= 1

            return curr_node.data

    def isEmpty(self):
        if (self.indx < 0):
            return True
        else:
            return False

    def peek(self):
        return self.nth.data

# class DoublyLinkedList:

def main():
    # A singly linked list
    singly = SinglyLinkedList()
    singly.push('cat')
    singly.push('rabbit')
    singly.push('fish')
    singly.push('ghoti')
    print(singly.length())
    print(singly.findx(0))
    print(singly.findx(1))
    print(singly.isEmpty())
    print(singly.findx(2))
    print(singly.findx(3))
    print(singly.peek())
    singly.pop()
    print(singly.findx(2))
    for i in range(singly.length()):
        singly.pop()
    print(singly.length())
    print(singly.isEmpty())
    print(singly.peek())

if __name__ == '__main__':
    main()

