class Node:
    def __init__(self, data, prev_node, next_node):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        return 'Data: {}\n Previous Node: {}\n Next Node: {}'.format(
                self.data, self.prev_node, self.next_node)

    def next(self):
        return self.next_node

    def prev(self):
        return self.prev_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_prev(self, new_prev):
        self.prev_node = new_prev


class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data, None, None)
        new_node.set_next(self.head)
        self.head = new_node

    def pop(self):
        pass

def main():
    pass
    a = Node('dog', None, 0)
    print(a)

    doubly = doublyLinkedList()
    print(doubly.push('dog'))
    doubly = doublyLinkedList()
    print(doubly.push('cat'))
    doubly = doublyLinkedList()
    print(doubly.push('rabbit'))

if __name__ == '__main__':
    main()
