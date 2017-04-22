#!/usr/bin/python3

# class AdjacencyMatrix:
#     def __init__(self, size=10):
#         self.size = size
#         self.matrix = {
#                       }

def depth(start, graph):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)

            for x in graph[node]:
                stack.append(x)

    return visited

def breadth(start, graph):
    queue = [start]
    visited = []

    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            for x in graph[node]:
                queue.insert(0, x)

    return visited

def main():
           # # A  B  C  D  E  H  I  J  K  L  M
    # tree = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], # A
           #  [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], # B
           #  [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0], # C
           #  [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], # D
           #  [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0], # E
           #  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], # H
           #  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], # I
           #  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], # J
           #  [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1], # K
           #  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], # L
           #  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]] # M

           #  # A  B  C  D  E  F  G  H  I  J
    # graph = [[0, 1, 0, 1, 0, 0, 0, 0, 1, 0], # A
           #   [1, 0, 1, 1, 1, 0, 0, 0, 0, 0], # B
           #   [0, 1, 0, 0, 1, 1, 0, 0, 0, 0], # C
           #   [1, 1, 0, 0, 1, 0, 1, 0, 0, 0], # D
           #   [0, 1, 1, 1, 0, 1, 1, 1, 0, 0], # E
           #   [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], # F
           #   [0, 0, 0, 1, 1, 0, 0, 1, 1, 1], # G
           #   [0, 0, 0, 0, 1, 1, 1, 0, 0, 1], # H
           #   [1, 0, 0, 0, 0, 0, 1, 0, 0, 1], # I
           #   [0, 0, 0, 0, 0, 0, 1, 1, 1, 0]] # J

    tree = {
            'a':['b'],
            'b':['a','c','d','e'],
            'c':['b','h','i'],
            'd':['b','j'],
            'e':['b','k'],
            'h':['c'],
            'i':['c'],
            'j':['d'],
            'k':['e','l','m'],
            'l':['k'],
            'm':['k']
           }

    graph = {
        'A':['B','D','I'],
        'B':['A','D','C','E'],
        'C':['B','E','F'],
        'D':['A','B','E','G'],
        'E':['C','D','F','G'],
        'F':['C','E','H'],
        'G':['D','E','H','I','J'],
        'H':['E','F','G','J'],
        'I':['A','G','J'],
        'J':['G','H','I'],
        }

    print(depth('a', tree))
    print(depth('a', graph))
    print(breadth('A', tree))
    print(breadth('A', graph))

if __name__=="__name__":
    main()
