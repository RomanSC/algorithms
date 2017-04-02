#!/usr/bin/python3
""" parse-tree.py | Sun, Apr 02, 2017 | Roman S. Collins

    An example of a parse tree implementation in Python.

"""
from classtreedatastructure import *


def build_tree(exp):
    # Paren check
    # if not exp.startswith("("):
    #     exp = "(" + exp

    # if not exp.endswith(")"):
    #     exp = exp + ")"

    stack = []

    exp_node = Node("")
    cur_node = exp_node

    # Ugh... .split() does not understand parens
    exp_slice = []
    for i in exp:
        if not i == " ":
            exp_slice.append(i)

    for i in exp_slice:
        # print(i)

        if i == "(":
            cur_node.insert_left("")
            stack.append(cur_node)
            cur_node = cur_node.get_left()
            print(exp_node)
        elif i not in ["+", "-", "*", "**", "/", "//", "%"]:


def add(self, a, b):
    return a + b

def sub(self, a, b):
    return a - b

def mul(self, a, b):
    return a * b

def div(self, a, b):
    return a / b

def floordiv(self, a, b):
    return a // b

def mod(self, a, b):
    return a % b

def pow(self, a, b):
    return a ** b

def main():
    parsestring = "(2 + 3 * 7 + 3 * 5 * (3 + 6 * (4 + 5)))"
    proof = 2 + 3 * 7 + 3 * 5 * (3 + 6 * (4 + 5))

    mytree = build_tree(parsestring)
    print(mytree)

if __name__ == "__main__":
    main()
