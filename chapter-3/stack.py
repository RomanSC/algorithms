""" stack.py | Sat, Feb 11, 2017 | Roman S. Collins

    Stack API as seen in Problem Solving with Algorithms and Data Structures

"""
class Stack:
    def __init__(self):
        pass
        self.items = []

    def __str__(self):
        return self.for_str_method()


    def isEmpty(self):
        # True if list is empty
        # Text book example:
        # return self.items == []
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item=None):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        # Return nth element of the list
        # Text book example:
        # return self.items[len(self.items) - 1]
        # Mine:
        for i in range(len(self.items)):
            return self.items[i]

    def size(self):
        return len(self.items)

    def for_str_method(self):
        temp_list = []
        temp_list.append('[')

        for i in range(len(self.items)):
            if isinstance(i, str):
                #temp_list.append(' ')
                temp_list.append('\'')
                temp_list.append(self.items[i])
                temp_list.append('\'')
                #if i != self.items[i]:
                #    temp_list.append(' ')

            if isinstance(i, int):
                temp_list.append(' ')
                temp_list.append(str(self.items[i]))
                #if i != self.items[i]:
                #    temp_list.append(' ')

            if i != self.items[i]:
                temp_list.append(',')

        temp_list.append(']')
        #print(len(self.items))

        #print(temp_list)
        return (''.join(temp_list))

def main():
    # Test all methods
    s = Stack()
    print(s.isEmpty())
    s.push('dog')
    s.push(1)
    s.push('rabbit')
    print(s.peek())
    print(s.size())
    s.pop()
    print(s.peek())
    print(s.size())
    print(s)

if __name__ == '__main__':
    main()
