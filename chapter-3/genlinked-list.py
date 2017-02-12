"""
"""
apoint, bpoint = 0, 1

class Node:
    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.point_forward = next_node

    def __str__(self):
        return self.data, self.prev_node, self.next_node

    def gen_node(self, data=None, prev_node=None, next_node=None):
        global apoint, bpoint
        while True:
            apoint += 1
            bpoint += 1

            yield apoint, bpoint

class doublyLinkedlist:
    def __init__(self):
        pass

    def __str__(self):
        return str(self.generate)

    def gen_elements(self, n_elements, item=''):
        self.generate = Node().gen_node(data=item, prev_node=apoint, next_node=bpoint)
        for i in range(n_elements):
            next(self.generate)

        return self.generate

"""
def generator():
    global apoint, bpoint
    while True:
        apoint += 1
        bpoint += 1

        yield apoint, bpoint

def gen(n):
    generate = generator()
    for i in range(n):
        next(generate)

    return apoint, bpoint
"""

def main():
    doubly = doublyLinkedlist()
    doubly.gen_elements(3, item='testdata')
    print(doubly)

if __name__ == '__main__':
    main()
