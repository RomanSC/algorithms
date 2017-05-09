#!/usr/bin/python3
""" astar.py | Sun, May 07, 2017 | Roman S. Collins

    Explanation of A*:

        An A* implementation attempt in Python. For my A* implementation I
    chose to use heapq, a minimum binary heap.* Which can be used as a priority
    queue by placing elements into the heap lead by the given elements
    'F score.'* As the algorithm executes, elements are looped over scanning for
    neighbors of the current vertex/node. The current node is added to the
    closedset after it's neighbors have been scanned resembling the way that
    humans view an area as they decide how to walk to a specific location. This
    is why A*, which was invented so that a robot could navigate space, is often
    used in video games for mob AI.* The closedset is a set of coordinates,
    whose values have already been calculated.) They are placed into the min
    heap which swaps elements until the neighbor, now an element in the min heap,
    with the lowest F score becomes the 0th element in the min heap. With each
    loop of the algorithm a new current vertex/node is popped of the priority
    queue from the top, the 0th element. The process of scanning nodes, which
    some call a "frontier", in the openset happens repeatedly while the
    algorithm keeps track of where which vertexes came from forming the path.
    After the goal vertex is found the algorithm returns a list by
    reconstructing the path from where each vertex came from starting with the
    goal, which was just found.* Provided good implementation of the algorithm,
    an optimal path and often the most optimal path can be found in the reversed
    order of the path returned from counting backwards from the current to the
    starting vertex.


    Summary of my implementation:

        I mostly followed the along to a video of Sebastian Lague writing the
    algorithm in C# for Unity, the explaination and psuedocode therein was
    useful. I also had to get more familiar with coordinates which 3D modeling
    and programming my 2D game for Matt Ollis's games course challenged me to
    learn. I also followed along to a few other videos, like Computerphile
    explaination of A* which doesn't exactly use the best explaination for
    reasons I'll explain in the weaknesses section. Nor was Coding Train quite
    the best way to implement A* because the programmer from the video did not
    use a binary heap. They did however use a class for individual nodes where
    I used a class containing a dictionary representation of the graph. Popping
    from a min binary heap is O(1) if it's the 0th or top. Where using a list
    would be O(n + 1). (The number of items, plus poping off the individual
    item when found).

        Besides using a min heap, I used a dictionary to also hash which
    vertexes are currently in the min heap, because to search for a vertex low
    in the min heap is inefficient. The reason to do this would become more
    apparent as the number of vertices in the heap increases. I can expect that
    if searching the min heap is uncommon, the tradeoff will not be worth it.
    I'll have to test with and without it to determine whether that is true and
    worthwhile though.

        A* also struggles with breaking ties between vertexes with the same F
    score what occasionally happens, like in step #6 for the output of this
    program (if my improved heuristic is not used), the calculated F score
    between two points is the same, but they may not be heading in the right
    direction. To prioritize vertexes with the least difference in terms of
    direction I simply subtracted one unit vector from another, and subracted
    the sum of that expression from the F score. Much to my surprise it worked!

    Weaknesses to A* and notation:

        The Computerphile video I watched used a graph, which was not a grid.
    In the case of using A* to solve a grid, it won't be the most efficient
    algorithm for doing so. A* does not differentiate between obstacles or
    non-existant vertexes and so they effectively don't exist to the algorithm
    because they are ignored. So if a graph is solved using A* star, where the
    graph itself is ungridlike (shape) it would be similar in effect to
    inputting a grid to A* that contains lots of obstacles. If this is true, it
    is likely also true that A* is also most efficient in the case that the
    graph has many connected nodes particularly in the center. With the right
    heuristic, A* can find diagonal routes from a point a to a point b very
    efficiently. There are also issues with A* picking non-optimal routes,
    but I fixed that.

    Sources:

    - Python Software Foundation. Heap queue algorithm.
         https://docs.python.org/2/library/heapq.html

    - Wikipedia. A* search algorithm. Description.
         https://en.wikipedia.org/wiki/A*_algorithm#Description

    - Silva, Porfirlo. Shakey.
         https://www.youtube.com/watch?v=qXdn6ynwpiI

    - RedBlob Games. Implementation of A*.
         http://www.redblobgames.com/pathfinding/a-star/implementation.html

    - Lague, Sebastian. A* Pathfinding (E01: algorithm explaination).
         https://www.youtube.com/watch?v=-L-WgKMFuhE&feature=youtu.be&list=PLFt_AvWsXl0cq5Umv3pMC9SPnKjfp9eGW&t=131

    - Computerphile. A* (A Star) Search Algorithm.
         https://www.youtube.com/watch?v=ySN5Wnu88nE&t=216s

    - Coding Train. Coding Challenge 51.1: A* Pathfinding Algorithm - Part 1.
         https://www.youtube.com/watch?v=aKYlikFAV4k&t=1535s

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

    # if -1 < goal[0] > 0:
    #     origgoal = goal
    #     goal = (goal[0]-1, goal[1])
    # if -1 < goal[1] > 0:
    #     origgoal = goal
    #     goal = (goal[0], goal[1]-1)

    print("Searching for {}...".format(goal))

    openset = [] # Binary tree for efficiently ordering of next vertexes
    # Hash table for checking, is __ in openset? efficiently.
    inopenset = {}
    heappush(openset, (0, start))
    inopenset[start] = True
    closedset = {}

    camefrom = {}
    camefrom[start] = None

    g_cost = {}
    h_cost = {}
    f_cost = {}

    f_cost[start] = 0

    while openset:
        current = heappop(openset)[1]
        inopenset.pop(current)

        if current == (goal[0]-1, goal[1]-1):
            print("\nFOUND:", current)
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

            if neighbor not in camefrom:
                camefrom[neighbor] = current

            # if neighbor == goal:
            #     camefrom[neighbor] = current
            #     heappush(openset, (0, neighbor))
            #     inopenset[neighbor] = True
            #     continue

            if neighbor not in g_cost:
                temp_g = euclidian_heuristic(neighbor, start)
                g_cost[neighbor] = temp_g

            if neighbor not in h_cost:
                temp_h = euclidian_heuristic(neighbor, (goal[0]-1, goal[1]-1))
                h_cost[neighbor] = temp_h - directional_heuristic(current, neighbor, goal)

            f_cost[neighbor] = g_cost[neighbor] + h_cost[neighbor]
            if neighbor not in inopenset:
                heappush(openset, (f_cost[neighbor], neighbor))
                inopenset[neighbor] = True

        closedset[current] = None

        print("\nCurrent: {}".format(current))
        try:
            print("Camefrom: {}".format(camefrom[current]))
        except KeyError:
            pass
        print("Camefrom: {}".format(camefrom))
        print("\nNeighbors: {}".format(get_neighbors(current, boundary)))
        print("\nOpenset: {}".format(openset))
        print("Closedset: {}".format(closedset))
        print("\nG cost: {}".format(g_cost))
        print("H cost: {}".format(h_cost))
        print("F cost: {}".format(f_cost))

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
    print(h)
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

    print("\nFinding neighbors...")
    print("Vertex:", vertex)
    print("Boundary:", boundary)
    print("Done: {}".format(neighbors))

    return neighbors

def reconstruct_path(start, goal, camefrom):
    print("\n", camefrom)
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
    print(graph)

    print("\nTests:\n")
    print("\nStart: {}".format(graph[start]))
    print("Goal: {}".format(graph[(goal[0]-1, goal[1]-1)]))

    # Approximate
    ihtest = euclidian_heuristic(start, goal)
    # Returns float, so hypothetically more accurate when comparing vertexes
    fhtest = euclidian_heuristic(start, goal)
    print("\nEuclidean euclidian_heuristic check: {} or {}", ihtest, fhtest)

    gntest = get_neighbors((4, 4), (8, 8))
    print("\nGet neighbors function check: {}".format(gntest))

    # Implementation
    path, camefrom = astar(graph, start, goal)
    print("\nPath: {}".format(path))

    print("\n")
    slides = visual_slides(path, start, goal, width, height, obstacles)
    for slide in range(len(slides)):
        print("Step #{}:".format(slide))
        print(slides[slide])

    # print("\n", camefrom)

if __name__ == "__main__":
    main()
