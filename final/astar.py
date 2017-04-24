#!/usr/bin/python3
""" astar.py | Sat, Apr 22, 2017 | Roman S. Collins

    A* is a shortest path search algorithm. It is essentially Djikstra's
    algorithm yet tuned for speed by giving the algorithm a heuristic. In this
    case the heuristic is the distance to point E from the current node plus the
    weight of the current node, if the current node is S, the distance is 10.
    The weight could be any value producing a range of desired behavior, one
    example could be setting the weight to a value time, an A* implementation
    could consider distance and time as it's heuristic to determine the shortest
    route.

    Sources:

    A* Algorithm -- Wikipedia:


    A* -- Computerphile
    https://www.youtube.com/watch?v=ySN5Wnu88nE&t=619s

    Time Complexity of Python builtin "List" -- Stack Overflow:
    https://stackoverflow.com/questions/1296511/efficiency-of-using-a-python-list-as-a-queue

    (...or why I chose to use a deque instead of a python list,
    O(n) vs. O(1) for deque or .pop(0), with a deque poping is
    much faster, closer to the desired behavior.)

    Python Queue vs. collections deque:
    https://stackoverflow.com/questions/717148/queue-queue-vs-collections-deque

    ...and a bunch of videos:
    https://www.youtube.com/watch?v=J-ilgA_XNI0

"""
from collections import deque
from math import inf

#from graphics import *
import graphics as gfx
import time, sys

# Used for debugging
from termcolor import colored

width =  400
height = 400
fps = 60

# class Vert:
#     def __init__(self):
#         self.f = 0
#         self.g = 0
#         self.h = 0

def heuristic():
    pass

def astar(graph, start, goal):
    openset = [] # LIFO queue
    openset.append(start)

    # Testing
    # openset.append("A")
    # openset.append("B")
    # openset.append("C")
    # openset.append(goal)
    # openset.append("D")
    # openset.append("H")
    # openset.append(goal)

    closedset = []
    path = []

    # "For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, cameFrom will eventually contain the
    # most efficient previous step." -- Wikipedia

    # In other words:
    # This is the lowest weights for each node, in the case of the computerphile graph
    # there can be multiple answers for each node, so I made a dict of lists, and
    # will choose whichever item depending on further investigation

    # Holy crap that's fragile and hard to write...
    fromkeys = {}
    fromvals = {}
    for x in graph:
        # print(x)
        fromkeys[x] = []
        fromvals[x] = []

    # print(graph)
    for key, val in graph.items(): # For each vertice

        # low = (inf, inf)
        if isinstance(val, dict): # The vertices children
            # print(colored(("KEY:", key), "green"))
            # print("VAL:", val)
            # print()

            # low = (inf, inf)
            low = (inf, inf)
            lastval = None
            for k, v in val.items():
                if v != inf:
                # print("{} {}".format(key, ">"*3))
                # print(graph[k])
                # print("{} {}".format(key, "<"*6))
                    # print(colored((k, v), "yellow"))
                    if v <= low[1]:
                        # print(colored((k, v), "red"))
                        low =  (k, v)
                        fromkeys[key].append(k)
                        fromvals[key].append(v)

                        if lastval != None and v < lastval:
                            # print(v)
                            fromkeys[key] = [k]
                            fromvals[key] = [v]
                        # elif lastval != None and v <= lastval:
                        #     fromkeys[key].append(k)

                        lastval = v
                # if lastval != None and v < lastval:
                #     print(lastval)
            # print()

    print("FROMKEYS:", fromkeys)
    print("FROMVALS:", fromvals)

    g_score = {}
    for x in graph:
        g_score[str(x)] = inf
    g_score[start] = 0
    # print(g_score)

    f_score = {}
    for x in graph:
        f_score[str(x)] = inf
    # print(f_score)

    current = None
    while openset: # while openset not empty
        # print("Searching... ")
        # print("OPENED  :", openset)
        # print("CLOSED  :", closedset)
        # print("PATH    :", path)
        # print()
        # print("CURRENT :", current)

        # If the goal is found stop
        if current == goal:
            # print("{} == {}: {}".format(current, goal, current == goal))
            # TODO:
            # Here's where return path should go
            return path, current
        # else:
        #     print("{} == {}: {}".format(current, goal, current == goal))
        current = openset.pop(0)
        closedset.append(current)

        # # Came From
        # low = (inf, inf)
        # for k, v in graph[current].items():
        #     if v < low[1] and k not in closedset:
        #         low = (k, v)

        # Find the lowest weighted item (fscore)
        low = (inf, inf)
        for k, v in graph[current].items():
            if v < low[1] and k not in closedset:
                low = (k, v)

        path.append(current)
        # openset.remove(current)
        openset.append(low[0])

        # Compute g_score or distance from goal
        # for each vertice
        itera = -1
        for x in path:
            # print(x, itera)
            if g_score[x] == inf:
                g_score[x] = itera
            itera += 1
        # print(g_score)
        # print(g_score[current])
        # print()



    while openset:
        ilow = 0;
        for x in range(len(openset)):
            pass


def main():
    # Adjacency matrix using dictionaries
    # where weight can be represented by
    # dictionary values greater than 0
    graph = {
             "S": {"S": 0, "A": 7, "B": 2, "C": 3,
                   "D": 0, "H": 0, "L": 0, "F": 0,
                   "G": 0, "I": 0, "J": 0, "E": 0, "K": 0},

             "A": {"S": 7, "A": 0, "B": 3, "C": 0,
                   "D": 4, "H": 0, "L": 0, "F": 0,
                   "G": 0, "I": 0, "J": 0, "E": 0, "K": 0},

             "B": {"S": 2, "A": 3, "B": 0, "C": 0,
                   "D": 4, "H": 1, "L": 0, "F": 0,
                   "G": 0, "I": 0, "J": 0, "E": 0, "K": 0},

             "C": {"S": 3, "A": 0, "B": 0, "C": 0,
                   "D": 0, "H": 0, "L": 2, "F": 0,
                   "G": 0, "I": 0, "J": 0, "E": 0, "K": 0},

             "D": {"S": 0, "A": 4, "B": 4, "C": 0,
                   "D": 0, "H": 0, "L": 0, "F": 5,
                   "G": 0, "I": 0, "J": 0, "E": 0, "K": 0},

             "H": {"S": 0, "A": 0, "B": 1, "C": 0,
                   "D": 0, "H": 0, "L": 0, "F": 3,
                   "G": 2, "I": 0, "J": 0, "E": 0, "K": 0},

             "L": {"S": 0, "A": 0, "B": 0, "C": 2,
                   "D": 0, "H": 0, "L": 0, "F": 0,
                   "G": 0, "I": 4, "J": 4, "E": 0, "K": 0},

             "F":{"S": 0, "A": 0, "B": 0, "C": 0,
                   "D": 5, "H": 3, "L": 0, "F": 0,
                   "G": 0, "I": 0, "J": 0, "E": 0, "K": 0},

             "G": {"S": 0, "A": 0, "B": 0, "C": 0,
                   "D": 0, "H": 2, "L": 0, "F": 0,
                   "G": 0, "I": 0, "J": 0, "E": 2, "K": 0},

             "I": {"S": 0, "A": 0, "B": 0, "C": 0,
                   "D": 0, "H": 0, "L": 4, "F": 0,
                   "G": 0, "I": 0, "J": 6, "E": 0, "K": 4},

             "J": {"S": 0, "A": 0, "B": 0, "C": 0,
                   "D": 0, "H": 0, "L": 4, "F": 0,
                   "G": 0, "I": 6, "J": 0, "E": 0, "K": 4},

             "E": {"S": 0, "A": 0, "B": 0, "C": 0,
                   "D": 0, "H": 0, "L": 0, "F": 0,
                   "G": 2, "I": 0, "J": 0, "E": 0, "K": 5},

             "K": {"S": 0, "A": 0, "B": 0, "C": 0,
                   "D": 0, "H": 0, "L": 0, "F": 0,
                   "G": 0, "I": 4, "J": 4, "E": 5, "K": 0},
             }

    a = "S"
    b = "E"

    # graph = {
    #          "S":{"S": 0, "A": 1, "B": 1, "C": 1,
    #               "D": 0, "H": 0, "L": 0, "F": 0,
    #               "G": 0, "I": 0, "J": 0, "E": 0, "K": 0},

    #          "A":{"S": 1, "A": 0, "B": 1, "C": 0,
    #               "D": 1, "H": 0, "L": 0, "F": 0,
    #               "G": 0, "I": 0, "J": 0, "E": 0, "K": 0},

    #          "B":{"S": 1, "A": 1, "B": 0, "C": 0,
    #               "D": 4, "H": 1, "L": 0, "F": 0,
    #               "G": 0, "I": 0, "J": 0, "E": 0, "K": 0},

    #          "C":{"S": 1, "A": 0, "B": 0, "C": 0,
    #               "D": 0, "H": 0, "L": 1, "F": 0,
    #               "G": 0, "I": 0, "J": 0, "E": 0, "K": 0},

    #          "D":{"S": 0, "A": 1, "B": 1, "C": 0,
    #               "D": 0, "H": 0, "L": 0, "F": 1,
    #               "G": 0, "I": 0, "J": 0, "E": 0, "K": 0},

    #          "H":{"S": 0, "A": 0, "B": 1, "C": 0,
    #               "D": 0, "H": 0, "L": 0, "F": 1,
    #               "G": 1, "I": 0, "J": 0, "E": 0, "K": 0},

    #          "L":{"S": 0, "A": 0, "B": 0, "C": 1,
    #               "D": 0, "H": 0, "L": 0, "F": 0,
    #               "G": 0, "I": 1, "J": 1, "E": 0, "K": 0},

    #          "F":{"S": 0, "A": 0, "B": 0, "C": 0,
    #               "D": 1, "H": 1, "L": 0, "F": 0,
    #               "G": 0, "I": 0, "J": 0, "E": 0, "K": 0},

    #          "G":{"S": 0, "A": 0, "B": 0, "C": 0,
    #               "D": 0, "H": 1, "L": 0, "F": 0,
    #               "G": 0, "I": 0, "J": 0, "E": 1, "K": 0},

    #          "I":{"S": 0, "A": 0, "B": 0, "C": 0,
    #               "D": 0, "H": 0, "L": 1, "F": 0,
    #               "G": 0, "I": 0, "J": 1, "E": 0, "K": 1},

    #          "J":{"S": 0, "A": 0, "B": 0, "C": 0,
    #               "D": 0, "H": 0, "L": 1, "F": 0,
    #               "G": 0, "I": 1, "J": 0, "E": 0, "K": 1},

    #          "E":{"S": 0, "A": 0, "B": 0, "C": 0,
    #               "D": 0, "H": 0, "L": 0, "F": 0,
    #               "G": 1, "I": 0, "J": 0, "E": 0, "K": 1},

    #          "K":{"S": 0, "A": 0, "B": 0, "C": 0,
    #               "D": 0, "H": 0, "L": 0, "F": 0,
    #               "G": 0, "I": 1, "J": 1, "E": 1, "K": 0},
    #          }

    graph = {
             "S": {"S": inf, "A": 7, "B": 2, "C": 3,
                   "D": inf, "H": inf, "L": inf, "F": inf,
                   "G": inf, "I": inf, "J": inf, "E": inf, "K": inf},

             "A": {"S": 7, "A": inf, "B": 3, "C": inf,
                   "D": 4, "H": inf, "L": inf, "F": inf,
                   "G": inf, "I": inf, "J": inf, "E": inf, "K": inf},

             "B": {"S": 2, "A": 3, "B": inf, "C": inf,
                   "D": 4, "H": 1, "L": inf, "F": inf,
                   "G": inf, "I": inf, "J": inf, "E": inf, "K": inf},

             "C": {"S": 3, "A": inf, "B": inf, "C": inf,
                   "D": inf, "H": inf, "L": 2, "F": inf,
                   "G": inf, "I": inf, "J": inf, "E": inf, "K": inf},

             "D": {"S": inf, "A": 4, "B": 4, "C": inf,
                   "D": inf, "H": inf, "L": inf, "F": 5,
                   "G": inf, "I": inf, "J": inf, "E": inf, "K": inf},

             "H": {"S": inf, "A": inf, "B": 1, "C": inf,
                   "D": inf, "H": inf, "L": inf, "F": 3,
                   "G": 2, "I": inf, "J": inf, "E": inf, "K": inf},

             "L": {"S": inf, "A": inf, "B": inf, "C": 2,
                   "D": inf, "H": inf, "L": inf, "F": inf,
                   "G": inf, "I": 4, "J": 4, "E": inf, "K": inf},

             "F":{"S": inf, "A": inf, "B": inf, "C": inf,
                   "D": 5, "H": 3, "L": inf, "F": inf,
                   "G": inf, "I": inf, "J": inf, "E": inf, "K": inf},

             "G": {"S": inf, "A": inf, "B": inf, "C": inf,
                   "D": inf, "H": 2, "L": inf, "F": inf,
                   "G": inf, "I": inf, "J": inf, "E": 2, "K": inf},

             "I": {"S": inf, "A": inf, "B": inf, "C": inf,
                   "D": inf, "H": inf, "L": 4, "F": inf,
                   "G": inf, "I": inf, "J": 6, "E": inf, "K": 4},

             "J": {"S": inf, "A": inf, "B": inf, "C": inf,
                   "D": inf, "H": inf, "L": 4, "F": inf,
                   "G": inf, "I": 6, "J": inf, "E": inf, "K": 4},

             "E": {"S": inf, "A": inf, "B": inf, "C": inf,
                   "D": inf, "H": inf, "L": inf, "F": inf,
                   "G": 2, "I": inf, "J": inf, "E": inf, "K": 5},

             "K": {"S": inf, "A": inf, "B": inf, "C": inf,
                   "D": inf, "H": inf, "L": inf, "F": inf,
                   "G": inf, "I": 4, "J": 4, "E": 5, "K": inf},
             }

    astar(graph, a, b)

if __name__=="__main__":
    main()
