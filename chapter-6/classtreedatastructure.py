""" class-tree-data-structure.py | Set, Apr 01, 2017 | Roman S. Collins

    An implementation of tree data structure in Python utilizing
    class objects for each node.

"""
class Node:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.left = left
        self.right = right
        self.__indent__ = 0

    def insert_left(self, data):
        if self.left == None:
            self.left = Node(data)
        else:
            t = Node(data)
            t.left = self.left
            self.left = t

    def insert_right(self, data):
        if self.right == None:
            self.right = Node(data)
        else:
            t = Node(data)
            t.right = self.right
            self.right = t

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    # Human readable version of __str__ method
    def __str__(self):
        indent = self.__indent__ + 4
        if self.left == None:
            left_string = "[]"
        else:
            self.left.__indent__ = indent
            left_string = str(self.left)
            self.left.__indent__ = 0

        if self.right == None:
            right_string = "[]"
        else:
            self.right.__indent__ = indent
            right_string = str(self.right)
            self.right.__indent__ = 0

        return "[{},\n{}{},\n{}{}]".format(self.data,
                                           " " * indent, left_string,
                                           " " * indent, right_string)

    # def __str__(self):
    #     if self.left == None:
    #         left_string = "[]"
    #     else:
    #         left_string = str(self.left)

    #     if self.right == None:
    #         right_string = "[]"
    #     else:
    #         right_string = str(self.right)

    #     return "[{}, {}, {}]".format(self.data, left_string, right_string)

def main():
    root = Node("a")
    root.insert_left("b")
    root.left.insert_right("d")
    root.insert_right("c")
    root.right.insert_left("e")
    root.right.insert_right("f")

    print(root)

if __name__ == "__main__":
    main()
