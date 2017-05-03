#!/usr/bin/python3

# from heapq import heappush as hpush
# from heapq import heappop as hpop

import heapq

from math import inf
from math import sqrt

import random

# Only need to consider the Euclidian
# Distance for
def euclidian_heuristic(y1, y2, x1, x2):
    return sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2)

def astar(graph, start, goal):
    started = []
    started.append(start)

    closed = []

    path = {}

    while started:
        pass


def new_grid(start, goal, width=5, height=5, rand_obst=False):
    chance = [False, False, True]

    if not rand_obst:
        grid = [[(x, y) for x in range(width)] for y in range(height)]
        grid[0][0] = st

    elif rand_obst:
        # return [[random.choice(["🍕", (x, y)]) for x in range(width)] for y in range(height)]
        # grid = []
        # for y in range(height):
        #     inner = []
        #     for x in range(width):
        #         # ch = random.choice(chance)
        #         # if ch and x != 0 and y != 0 and x != width -1 and y != width - 1:
        #         #     grid.append("🍕")
        #         # else:
        #         #     grid.append((x, y))


        #         ch = random.choice(chance)
        #         if x != start[0] and y != start[1] and x != goal[0] - 1 and x != goal[1] - 1: # if not start or goal
        #             inner.append((x, y))

        #         if x == start[0] and y == start[1]:
        #             inner.append("S")

        #         if x == goal[0] and y == goal[1]:
        #             inner.append("G")

        #         else:
        #             # inner.append("e")
        #             inner.append((x, y))
        #     grid.append(inner)

        grid = []
        for y in range(height):
            inner = []
            for x in range(width):
                cur = (x, y)
                # inner.append((x, y))
                if cur == start:
                    inner.append("_")

                if cur == (goal[0]-1, goal[1]-1):
                    inner.append("$")

                if cur != start and cur != (goal[0]-1, goal[1]-1):
                    # inner.append((x, y))
                    ch = random.choice(chance)
                    if ch:
                        inner.append("🍕")
                    else:
                        inner.append((x, y))

                # else:
                #     # inner.append("e")
                #     inner.append((x, y))

            grid.append(inner)

        return grid

def main():
    width = 8
    height = 8

    start = (0, 0)
    goal = (width, height)

    grid = new_grid(start, goal, width, height)

    for x in grid:
        print(x)


    y1, x1 = start[0], start[1]
    y2, x2 = goal[0], goal[1]
    htest = euclidian_heuristic(y1, y2, x1, x2)

    print(htest)

if __name__ == "__main__":
    main()
