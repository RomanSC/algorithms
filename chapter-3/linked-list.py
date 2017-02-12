""" linked-list.py | Mon, Feb 6, 2017 | Roman S. Collins

    Demonstrating a linked list in Python.

"""
class Node:
    # Data is the data
    # Node is the pointer
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.next_node, ':', self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()

        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
            if current == None:
                raise ValueError('Data not in list.')
            return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

def main():
    pass

if __name__ == '__main__':
    main()
