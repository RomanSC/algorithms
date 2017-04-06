#!/usr/bin/python3
""" parse-tree.py | Sun, Apr 02, 2017 | Roman S. Collins

    An example of a parse tree implementation in Python.

"""
from classtreedatastructure import *

def try_int(mystr):
    try:
        mystr = int(mystr)
        return True
    except ValueError:
        return False

def format_exp(exp, accept_chars=["(", "+", "-", "*", "**", "/", "//", "%", "^", ")"]):
    """ Adapted from: Source, Stack Overflow:
        https://stackoverflow.com/questions/13132959/python-math-expression-parsing

        Code from book is borken ass hell...

        Can't just go about .split()'ing everything.. did they even test their
        code!?
    """
    exp_slice = []

    for x in range(len(exp)):
        if exp[x].isdigit():
            try:
                if exp_slice[x-1].isdigit():
                    exp_slice[x-1] += exp[x]
                else:
                    exp_slice.append(exp[x])
            except IndexError:
                exp_slice.append(exp[x])

        elif exp[x] in accept_chars:
            exp_slice.append(exp[x])

    print("Formatted expression: ", exp_slice)
    return exp_slice

def build_tree(exp):
    # Paren check
    # if not exp.startswith("("):
    #     exp = "(" + exp

    # if not exp.endswith(")"):
    #     exp = exp + ")"

    stack = []

    exp_node = Node("")
    stack.append(exp_node)
    cur_node = exp_node

    # Ugh... .split() does not understand parens
    # nor numbers greater than 9 as they
    # are multiple digits
    # exp_slice = []
    # for i in exp:
    #     if not i == " ":
    #         exp_slice.append(i)
    exp_slice = format_exp(exp)

    for i in exp_slice:
        if i == "(":
            cur_node.insert_left("")
            stack.append(cur_node)
            cur_node = cur_node.get_left()
        elif not i in ["+", "-", "*", "**", "/", "//", "%", "^", ")"]:
            cur_node.set_data(i)
            parent = stack.pop()
            cur_node = parent
        elif i in ["+", "-", "*", "**", "/", "//", "%", "^"]:
            cur_node.set_data(i)
            cur_node.insert_right("")
            stack.append(cur_node)
            cur_node = cur_node.get_right()
        elif i == ")":
            try:
                cur_node = stack.pop()
            except IndexError:
                pass
        else:
            raise ValueError

    return exp_node


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

def xor(self, a, b):
    return a ^ b

def evaluate(atree):
    operators = {"+": add, "-": sub, "*": mul, "/": div, "//": floordiv, "%": mod, "^": xor}

    meleft = atree.get_left()
    meright = atree.get_right()

    if meleft and meright:
        fn = operators[atree.get_data()]
        return fn(evaluate(meleft), evaluate(meright))
    else:
        return atree.get_data()

def main():
    pass
    parsestring = "(2 + 3 * 7 + 3 * 5 * (3 + 6 * (4 + 5)))"
    proof = 2 + 3 * 7 + 3 * 5 * (3 + 6 * (4 + 5))

    parsestring = "((2+3) * (7 + 3)))"

    mytree = build_tree(parsestring)
    print(mytree)

    # myeval = evaluate(mytree)
    # print(myeval)
    # print(proof)

if __name__ == "__main__":
    main()
