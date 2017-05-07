#!/usr/bin/python3

# from heapq import heappush as hpush
# from heapq import heappop as hpop
import random
from heapq import heappush, heappop, heapify
from math import inf, sqrt
# from math import sqrt

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

""" Source:

    A* Pathfinding (E03: algorithm implementation):
    https://youtu.be/mZfyt03LDH4?t=462

"""
def astar(grid, start, goal, start_sym=" @ ", goal_sym=" * ", obst_sym=chr(0x2588)):
    openset = []
    closedset = {}
    openset.append(start)
    boundry = max(len(grid), len(grid[0]))
    boundry = (boundry, boundry)
    # print("Search boundry:", boundry)

    g_cost = {}
    f_cost = {}
    h_cost = None

    camefrom = {}

    current = None
    while openset:
        if current == goal:
            pass
            print("FOUND!")

        if current in closedset:
            pass
            print("current in closedset")

        current = openset.pop(0)
        closedset[current] = True

        neighbors = get_neighbors(current, boundry)
        # print("\nNeighbors for {}: ".format(current), neighbors)

        g_cost[current] = distance(start[0], start[1], current[0], current[0])
        # g_cost[current] = distance(0, 0, 8, 3)
        # print("Current g_cost for {}:".format(current), g_cost[current])

        for neighbor in neighbors:
            temp_g = distance(start[0], start[1], current[0], current[0])
            # print("temp_g:", temp_g)
            # if not neighbor in closedset and not neighbor == obst_sym:
            # if grid[neighbor[0]-1][neighbor[1]-1] == obst_sym:
            if obst_sym in grid[neighbor[0]-1][neighbor[1]-1]:
                    print("obst_sym in a neighbor", neighbor)
                    print("Neighbor:", neighbor[0], neighbor[1])
                    print("Grid:", grid[neighbor[0]+1][neighbor[1]+1])
                    closedset[neighbor] = True
                    print()
            else:
                f_cost[current] = None # Heuristic

                #
                if not neighbor in openset:
                    openset.append(neighbor)

        # print("\nClosed set:", closedset)

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
             obst_sym=chr(0x2588), specified=False):

    if specified:
        grid = [[(x, y) for x in range(width)] for y in range(height)]
        grid[start[1]][start[0]] = start_sym
        grid[goal[1]-1][goal[0]-1] = goal_sym

        for y in range(len(grid)):
            obst_num = 0 # Count the number of obstacles
            # print(obst_num)
            for x in range(len(grid[y])):
                # print(isinstance(grid[y][x], tuple))
                # print(specified)
                # print(isinstance(specified, dict))
                # print(type(specified))
                # print()
                if isinstance(specified, list):
                    for obstacle in specified:
                        if obstacle != start and obstacle != goal:
                            if obstacle == grid[y][x]:
                                grid[y][x] = str(obst_sym) * zero_div(4, obst_num) # So grid printout looks nice
                else:
                    print("{} is not a list, specified needs to \
                           be a list to define specific obstacles".format(specified))

        return grid

    elif not rand_obst:
        grid = [[(x, y) for x in range(width)] for y in range(height)]
        grid[start[0]][start[1]] = start_sym
        grid[goal[0]-1][goal[1]-1] = goal_sym
        return grid

    # A grid representation using random obstactles
    elif rand_obst:
        chance = [False, False, True] # where 1/3 become obstacles

        grid = []
        obst_sum = 0
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
                        inner.append(str(obst_sym) * zero_div(4, obst_num))
                        obst_num += 1
                    else:
                        inner.append((x, y))

                elif cur == start:
                    # inner.append("____")
                    # inner.append(str(start_sym))
                    inner.append(start_sym)

                elif cur == (goal[0]-1, goal[1]-1):
                    inner.append(goal_sym)

            obst_sum += obst_num
            grid.append(inner)

        # print("Number of obstacles: {}".format(obstacles))
        return grid

def zero_div(a, b):
    if a or b == 0:
        return a
    else:
        return a / b

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
    goal = (8, 0)

    obstacles=[(0, 1), (0, 2), (0, 3),
               (1, 3), (2, 3), (3, 3),
               (4, 3), (6, 0), (6, 1),
               (6, 2), (6, 3), (6, 4),
               (6, 5), (6, 6)]

    grid = new_grid(start, goal, width, height, specified=obstacles)
    print_grid(grid)

    # print("\nStart position:", start)
    # print("Goal position:", goal)

    # y1, x1 = start[0], start[1]
    # y2, x2 = goal[0], goal[1]
    # htest = euclidian(x1, x2, y1, y2)

    # print("\nEuclidian distance check:", htest)

    # print("\nget_neighbors() test:")
    # print("Topleft: ", get_neighbors((0, 0), (xbound, ybound)))
    # print("Topright: ", get_neighbors((8, 0), (xbound, ybound)))
    # print("Bottomleft:", get_neighbors((0, 8), (xbound, ybound)))
    # print("Bottomright:", get_neighbors((8, 8), (xbound, ybound)))
    # print("Middle:", get_neighbors((4, 4), (xbound, ybound)))

    astar(grid, start, goal)

if __name__ == "__main__":
    main()
