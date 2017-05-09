#!/usr/bin/python3
""" astar.py | Sun, May 07, 2017 | Roman S. Collins

    See writeup.txt for explanation of implementation.

"""
from create_graph import GridGraph

import random
from heapq import *
from math import inf, sqrt, tan

""" Source:
    - Lague, Sebastian. A* Pathfinding (E03: algorithm implementation):
      https://youtu.be/mZfyt03LDH4?t=462

        "Heap elements can be tuples.
         This is useful for assigning
         comparison values (such as
         task priorities) alongside
         the main record being tracked"

         heapq is perfect because it
         is already a min heap
         implementation.

         let openset be a min heap,
         append tuples to openset
         to use the min heap for
         h_cost to search, tuples
         will consist of some heuristic
         value and the given coordinate
"""
def astar(graph, start, goal,
          start_sym="@", goal_sym="*",
          obst_sym=str(chr(0x2588))):

    boundary = (graph.width, graph.height)

    # print("Searching for {}...".format(goal))

    openset = [] # Binary tree for efficiently ordering of next vertexes
    heappush(openset, (0, start))
    closedset = {}

    camefrom = {}
    camefrom[start] = None

    g_cost = {}
    h_cost = {}
    f_cost = {}

    f_cost[start] = 0

    while openset:
        current = heappop(openset)[1]

        if current == (goal[0]-1, goal[1]-1):
            # print("\nFOUND:", current)
            # # return list(reconstruct_path(current, camefrom, start))
            # path = list(reconstruct_path(current, camefrom, start))
            # # path.append(current)
            # return path
            return list(reconstruct_path(start, goal, camefrom)), camefrom

        if current in closedset:
            continue

        # neighbors = get_neighbors(current, boundary)
        # print(neighbors)
        # for neighbor in neighbors:
        for neighbor in get_neighbors(current, boundary):
            if neighbor in closedset or obst_sym == graph[neighbor]:
                continue

            if goal_sym == graph[neighbor]: # Skip calculating if found
                camefrom[neighbor] = current
                heappush(openset, (0, neighbor))
                continue

            if neighbor not in camefrom:
                camefrom[neighbor] = current

            temp_g = euclidian_heuristic(neighbor, start)
            if neighbor not in g_cost or temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g

            temp_h = euclidian_heuristic(neighbor, (goal[0]-1, goal[1]-1))
            if neighbor not in h_cost or temp_h < h_cost[neighbor]:
                # h_cost[neighbor] = temp_h # without taking into account direction
                h_cost[neighbor] = temp_h - directional_heuristic(current, neighbor, goal)
                # h_cost[neighbor] = temp_h # without taking into account direction

            f_cost[neighbor] = g_cost[neighbor] + h_cost[neighbor]
            heappush(openset, (f_cost[neighbor], neighbor))

        closedset[current] = None

        # print("\nCurrent: {}".format(current))
        # try:
        #     print("Camefrom: {}".format(camefrom[current]))
        # except KeyError:
        #     pass
        # print("Camefrom: {}".format(camefrom))
        # print("\nNeighbors: {}".format(get_neighbors(current, boundary)))
        # print("\nOpenset: {}".format(openset))
        # print("Closedset: {}".format(closedset))
        # print("\nG cost: {}".format(g_cost))
        # print("H cost: {}".format(h_cost))
        # print("F cost: {}".format(f_cost))

"""
    Using Euclidean distance:

    Source:

    - 2D Distance Calculator -- calculatorsoup.com
      http://www.calculatorsoup.com/calculators/geometry-plane/distance-two-points.php

    - Euclidean distance can be used to check the distance of more than two points or
      a given number of points:
      https://en.wikipedia.org/wiki/Euclidean_distance
"""
def euclidian_heuristic(here, to, ret_int=True):
    if not ret_int:
        return sqrt(((here[0] - to[0]) ** 2) + ((here[1] - to[1]) ** 2))
    elif ret_int:
        return int(sqrt(((here[0] - to[0]) ** 2) + ((here[1] - to[1]) ** 2)))

""" Favor angles that get you closer to the goal.

    One normalized, unit, or direction (unsure of words I am supposed to use
    because trig is new to me) vector minus another should give the difference
    between the two angles.

"""
def directional_heuristic(current, neighbor, goal):
    cdx = current[1] - goal[1]
    cdy = current[0] - goal[0]
    ndx = neighbor[0] - goal[0]
    ndy = neighbor[1] - goal[1]
    h = sqrt(cdx ** 2 + cdy ** 2) - sqrt(ndx ** 2 + ndy ** 2)
    # print(h)
    return h

def get_neighbors(vertex, boundary):
    x, y = vertex[0], vertex[1]
    neighbors = [(xe, ye) for xe in range(x-1, x+2)
                          for ye in range(y-1, y+2)
                          if (-1 < x <= boundary[0]-1 and
                              -1 < y <= boundary[1]-1 and
                              (x != xe or y != ye) and
                              (-1 < xe <= boundary[0]-1) and
                              (-1 < ye <= boundary[1]-1))]

    # print("\nFinding neighbors...")
    # print("Vertex:", vertex)
    # print("Boundary:", boundary)
    # print("Done: {}".format(neighbors))

    return neighbors

def reconstruct_path(start, goal, camefrom):
    # print("\n", camefrom)
    path = [(goal[0]-1, goal[1]-1)]

    for vert in path:
        if start in path:
            break
        path.append(camefrom[vert])

    return reversed(path)

def visual_slides(path, start, goal, width, height, obstacles=None):
    slides = []

    for vert in path:
        slides.append(GridGraph(vert, goal, width, height, specified=obstacles))

    return slides

def main():
    width, height = 8, 8

    start = (0, 0)
    goal = (width, height)

    obstacles=[start, (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
               (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), goal]

    graph = GridGraph(start, goal, width, height, specified=obstacles)
    # print(graph)

    # print("\nTests:\n")
    # print("\nStart: {}".format(graph[start]))
    # print("Goal: {}".format(graph[(goal[0]-1, goal[1]-1)]))

    # Approximate
    ihtest = euclidian_heuristic(start, goal)
    # Returns float, so hypothetically more accurate when comparing vertexes
    fhtest = euclidian_heuristic(start, goal)
    # print("\nEuclidean euclidian_heuristic check: {} or {}", ihtest, fhtest)

    gntest = get_neighbors((4, 4), (8, 8))
    # print("\nGet neighbors function check: {}".format(gntest))

    # Implementation
    path, camefrom = astar(graph, start, goal)
    # print("\nPath: {}".format(path))

    print("\n")
    slides = visual_slides(path, start, goal, width, height, obstacles)
    for slide in range(len(slides)):
        print("Step #{}:".format(slide))
        print(slides[slide])

    # print("\n", camefrom)

if __name__ == "__main__":
    main()
