""" binary-heap.py | Thu, Mar 30, 2017 | Roman S. Collins

    A binary heap is and abstract data type for storing
    data in a tree which has a maximum of two children
    for each node.

    It's often used for implementing heapsort.

    https://en.wikipedia.org/wiki/Binary_heap

"""

# To find the children
# 2 * i + 1
# 2 * i + 2
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
         # 0
        # 1 2
      # 3 4 5 6
    # 7 8 9 10 11 12 13 14
  # 15 16

class NODE():
    def __init__(self, data=None, child1=None, child2=None):
        self.data = data
        self.child1 = child1
        self.child2 = child2
        self.__indent__ = 0

    def add1(self, data):
        self.child1 = node(data)
        return self.child1

    def add2(self, data):
        self.child2 = node(data)
        return self.child2

    # def print_node(self, level=0):
    #         print('\t' * level + repr(self.data))
    #         for child in self.children:
    #             child.print_node(level+1)

    def __str__(self):
        if self.child1 == None:
            child1_string = "[]"
        else:
            self.child1.__indent__ = + 1
            child1_string == str(self.child1)
            self.child1._indent = 0

        if self.child2 == None:
            self.child2.__indent__ = + 1
            child2_string = "[]"
            self.child2._indent = 0
        else:
            child2_string = str(self.child2)

        return "[{}, \n{}{}, \n{}{}]".format(
                self.value,
                "    " * self.__indent__, child1_string,
                "    " * self.__indent__, child2_string,)


def main():
    # # Root node
    # root = hnode()

    # # Root's children
    # root_child_1 = hnode()

    # root_child_1_child_1 = hnode()
    # root_child_1_child_2 = hnode()

    # root_child_2 = hnode()

    # root_child_2_child_1 = hnode()
    # root_child_2_child_2 = hnode()

    # # Attach
    # root.lchild = root_child_1
    # root.rchild = root_child_2
    # root_child_1.parent = root
    # root_child_2.parent = root

    # root_child_1.lchild = root_child_1_child_1
    # root_child_1.rchild = root_child_1_child_2
    # root_child_1_child_1.parent = root_child_1
    # root_child_1_child_2.parent = root_child_1

    # root_child_2.lchild = root_child_2_child_1
    # root_child_2.rchild = root_child_2_child_2
    # root_child_2_child_1.parent = root_child_2
    # root_child_2_child_2.parent = root_child_2

    # node = node(12)
    # one = node.add1(1)
    # seven = node.add2(7)
    # six = seven.add1(6)
    # three = seven.add2(3)

    #print(node)

if __name__ == "__main__":
    main()

