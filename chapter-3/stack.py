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

if __name__ == '__main__':
    main()
