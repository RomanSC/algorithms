#!/usr/bin/python3

# from heapq import heappush as hpush
# from heapq import heappop as hpop

import heapq

from math import inf
from math import sqrt

import random

"""
    Source:

    2D Distance Calculator -- calculatorsoup.com
    http://www.calculatorsoup.com/calculators/geometry-plane/distance-two-points.php

    Euclidian distance can be used to check the distance of more than two points as
    well

    https://en.wikipedia.org/wiki/Euclidean_distance
"""
def euclidian(x1, x2, y1, y2):
    return sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2)

def distance(x1, y1, x2, y2):
    dx, dy = abs(x1 - x2), abs(y1 - y2)
    return (dx, dy)

def astar(grid, start, goal):
    openset = []
    closedset = {}
    openset.append(start)
    boundry = max(len(grid), len(grid[0]))
    boundry = (boundry, boundry)
    print("Search boundry:", boundry)

    g_cost = {}
    f_cost = {}
    h_cost = None

    camefrom = []

    while openset:
        current = openset.pop(0)

        if current in closedset:
            print("current in closedset")

        closedset[current] = True

        if current == goal:
            print("FOUND!")

        neighbors = get_neighbors(current, boundry)
        print("\nNeighbors for {}: ".format(current), neighbors)

        g_cost[current] = distance(start[0], start[1], current[0], current[0])
        # g_cost[current] = distance(0, 0, 8, 3)
        print("Current g_cost for {}:".format(current), g_cost[current])

        for neighbor in neighbors:
            temp_g = distance(start[0], start[1], current[0], current[0])
            if neighbor not in closedset:
                f_cost[current] = None # Heuristic



        print("\nClosed set:", closedset)

def get_neighbors(vertice, boundry):
    x, y = vertice[0], vertice[1]
    xb, yb = boundry[0], boundry[1]

    # If position is top left
    if x == 0 and y == 0 and x <= xb and y <= yb:
        return [(x+1, y), (x, y+1), (x+1, y+1)]

    # Else if position is top right
    elif x >= 0 and y == 0 and x <= xb and y <= yb:
        return [(x-1, y), (x-1, y+1), (x, y+1)]

    # # Else if position is bottom left
    elif x == 0 and y >= 0 and x <= xb and y <= yb:
        return [(x, y-1), (x+1, y-1), (x+1, y)]

    # Else if position is bottom right
    elif x == xb and y == yb:
        return [(x-1, y-1), (x, y-1), (x-1, y)]

    # Else if it's anywhere else within the boundry
    elif x >= 0 and y >= 0 and x <= xb and y <= yb:
        return [(x-1, y-1), (x, y-1), (x+1, y-1),
                (x-1, y),             (x+1, y),
                (x-1, y+1), (x, y+1), (x+1, y+1)]

def new_grid(start, goal, width=5, height=5, \
             start_sym=" @ ", goal_sym=" * ", rand_obst=False, \
             obs_sym=chr(0x2588), from_list=False):

    if not from_list:
        if not rand_obst:
            grid = [[(x, y) for x in range(width)] for y in range(height)]
            grid[start[0]][start[1]] = start_sym
            grid[goal[0]-1][goal[1]-1] = goal_sym
            return grid

        # A grid representation using random obstactles
        elif rand_obst:
            chance = [False, False, True] # where 1/3 become obstacles

            grid = []
            obstacles = 0
            for y in range(height):
                inner = []
                obst_num = 0
                for x in range(width):
                    cur = (x, y)

                    if cur != start and cur != (goal[0]-1, goal[1]-1):
                        ch = random.choice(chance)
                        if ch:
                            # print(x)
                            # print(obst_num)
                            inner.append(str(obs_sym) * zero_div(4, obst_num))
                            obst_num += 1
                        else:
                            inner.append((x, y))

                    elif cur == start:
                        # inner.append("____")
                        # inner.append(str(start_sym))
                        inner.append(start_sym)

                    elif cur == (goal[0]-1, goal[1]-1):
                        inner.append(goal_sym)

                obstacles += obst_num

                grid.append(inner)

            print("Number of obstacles: {}".format(obstacles))

            return grid

        # TODO:
        # Obstacles from list
        elif from_list:
            grid = [[(x, y) for x in range(width)] for y in range(height)]
            grid[start[0]][start[1]] = start_sym
            grid[goal[0]-1][goal[1]-1] = goal_sym
            print(grid)

            return grid

def zero_div(a, b):
    if a or b == 0:
        return a
    else:
        return a / b

# TODO:
# Make function that uses grid generation
# and makes obsticles from a list to redraw
# each step taken
def print_grid(grid):
    for y in range(len(grid)):
        if y == 0:
            print("[" + str(grid[y]))
        elif y != len(grid)-1:
            print(grid[y])
        else:
            print(str(grid[y]) + "]")

def main():
    width = 8
    height = 8
    xbound = width
    ybound = height

    start = (0, 0)
    goal = (width, height)

    grid = new_grid(start, goal, width, height)

    print_grid(grid)

    print("\nStart position:", start)
    print("Goal position:", goal)

    y1, x1 = start[0], start[1]
    y2, x2 = goal[0], goal[1]
    htest = euclidian(x1, x2, y1, y2)

    print("\nEuclidian distance check:", htest)

    # print("\nget_neighbors() test:")
    # print("Topleft: ", get_neighbors((0, 0), (xbound, ybound)))
    # print("Topright: ", get_neighbors((8, 0), (xbound, ybound)))
    # print("Bottomleft:", get_neighbors((0, 8), (xbound, ybound)))
    # print("Bottomright:", get_neighbors((8, 8), (xbound, ybound)))
    # print("Middle:", get_neighbors((4, 4), (xbound, ybound)))

    astar(grid, start, goal)

if __name__ == "__main__":
    main()
