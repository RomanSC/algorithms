""" tree-data-structure.py | Tue, Mar 28, 2017 | Roman S. Collins
"""
class Leaf:
    def __init__(self, parent=None, childs=[]):
        self.parent = parent
        self.childs = childs

def main():
    root = Leaf()

    for n in range(3):
        root.childs.append(Leaf(parent=root))

    for x in root.childs:
        print(x)

if __name__ == "__main__":
    main()
