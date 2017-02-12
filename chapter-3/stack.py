""" stack-methods.py | Tue, Feb 07, 2017 | Roman S. Collins

    Stack "methods?" yes, methods I think...

    From Problem Solving with Algorithms and Data Structures.

"""
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items) - 1]

     def size(self):
         return len(self.items)

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    # while 0 or 1 or 2... shorter than
    # fullstring passed as args
    # assumed to be true
    while index < len(symbolString) and balanced:
        # if fullstring is ((()))
        # symbol is (
        symbol = symbolString[index]
        # True
        if symbol == "(":
            # add to top of stack
            s.push(symbol)
        # Otherwise ) or None
        # or not (
        else:
            # check if None
            if s.isEmpty():
                # if none, then
                # the string is not
                # balanced because
                # it's nothing
                balanced = False
            else:
                # If something
                # remove it
                s.pop()

        #index = index + 1
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
    # hmm..

def main():
    s = Stack()
    print(s.isEmpty())
    print(s.push(4))
    print(s.push('dog'))
    print(s.peek())
    print(s.push(True))
    print(s.size())
    print(s.isEmpty())
    print(s.push(8.4))
    print(s.pop())
    print(s.pop())
    print(s.size())
    # True
    print(parChecker('((()))'))
    # False
    print(parChecker('(()'))
    # True
    print(parChecker(''))

if __name__ == '__main__':
    main()
