""" list-tree-data-structure.py | Sat, Apr 01, 2017 | Roman S. Collins

    An implementation of a tree data structure utilizing Python lists
    as nodes.

"""
def node(data):
    return [data, [], []]

def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])

    return root

def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])

    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def main():

    x = node("a")
    insert_left(x, "b")
    insert_right(x, "c")
    insert_right(get_left_child(x), "d")
    insert_left(get_right_child(x), "e")
    insert_right(get_right_child(x), "f")
    print(x)

if __name__ == "__main__":
    main()

