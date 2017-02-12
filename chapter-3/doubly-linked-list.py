""" linked-lists.py | Thu, Feb 09, 2017 | Roman S. Collins
"""
class Node:
    def __init__(self, data=None, parent_pointer=None, child_pointer=None):
        self.data = data
        self.parent_pointer = parent_pointer
        self.child_pointer = child_pointer

    def __str__(self):
        return 'DATA: {}, PARENT: {}, CHILD: {}'.format(self.data, self.parent_pointer, self.child_pointer)

    def new(self, new_parent_pointer=None, new_child_pointer=None):
        self.parent_pointer = new_parent_pointer
        self.child_pointer = new_child_pointer

    def get_data(self):
        return self.data

    def get_parent(self):
        return self.parent_pointer

    def get_child(self):
        return self.child_pointer

class doublyLinked:
    def __init__(self):
        pass
        self.index = 0

    # TODO
    def push(self, data=None, parent_pointer=None, child_pointer=None):
        new_node = Node(data, parent_pointer, child_pointer)

    def pop(self):
        pass

def main():
    one_node = Node('testdata', parent_pointer=None, child_pointer=None)
    two_node = Node('testdata', parent_pointer=one_node, child_pointer=None)
    one_node.new(new_parent_pointer=None, new_child_pointer=two_node)

    # They are linked together so when I attempt to call print
    # an infinite loop runs in Node().__str__()

    print(one_node)

if __name__ == '__main__':
    main()
