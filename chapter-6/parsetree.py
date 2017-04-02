#!/usr/bin/python3
""" parse-tree.py | Sun, Apr 02, 2017 | Roman S. Collins

    An example of a parse tree implementation in Python.

"""
from classtreedatastructure import *

def add(self, a, b):
    return a + b

def sub(self, a, b):
    return a - b

def mul(self, a, b):
    return a * b

def div(self, a, b):
    return a / b

def mod(self, a, b):
    return a % b

def build_tree(exp):
    if not isinstance(exp, str):
        raise TypeError
        print("TypeError: Sorry, only use strings please!")
        exit()

    # Paren check
    if not exp.startswith("("):
        exp = "(" + exp

    if not exp.endswith(")"):
        exp = exp + ")"

    stack = []

    exp_slice = []

    exp_tree = Node("")
    cur_node = exp_tree

    # Ugh... .split() does not understand parens
    for i in exp:
        if not i == " ":
            exp_slice.append(i)

    print(exp_slice)

    for i in exp_slice:
        if i == "(":
            cur_node.insert_left("")
            stack.append(cur_node)
            cur_node = cur_node.get_left()

        elif not i in ["+", "-", "*", "/", "%", ")"]:
            cur_node.set_data(int(i))
            cur_node = stack.pop()

        elif i in ["+", "-", "*", "/", "%"]:
            cur_node.set_data(i)
            cur_node.insert_right("")
            stack.append(cur_node)
            cur_node = cur_node.get_right()

        elif i == ")":
            cur_node = stack.pop()

        else:
            raise ValueError

        return exp_tree

def eval_tree():
    pass

def main():
    parsestring = "(2 + 3 * 7 + 3 * 5 * (3 + 6 * (4 + 5)))"
    proof = 2 + 3 * 7 + 3 * 5 * (3 + 6 * (4 + 5))

    mytree = build_tree(parsestring)
    print(mytree)

if __name__ == "__main__":
    main()
