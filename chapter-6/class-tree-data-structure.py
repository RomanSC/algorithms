""" class-tree-data-structure.py | Set, Apr 01, 2017 | Roman S. Collins
"""
class Node:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.left = left
        self.right = right

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



def main():

if __name__ == "__main__":
    main()
