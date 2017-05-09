<p align="center"><strong><font size=36>A* Search Algorithm:</font></strong></p>
<pre>
<font face="Monospace">
Step #0:
X: {0: &#39@&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 0<br/>
X: {0: &#39█&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 1<br/>
X: {0: &#39█&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 2<br/>
X: {0: &#39█&#39, 1: &#39█&#39, 2: &#39█&#39, 3: &#39█&#39, 4: &#39█&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 3<br/>
X: {0: &#39_&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 4<br/>
X: {0: &#39_&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 5<br/>
X: {0: &#39_&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 6<br/>
X: {0: &#39_&#39, 1: &https://coderwall.com/p/iftc1q/centered-text-and-images-in-github-markdown#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39_&#39, 7: &#39*&#39} Y: 7<br/><font></pre>
<pre>
<font face="Monospace">
Step #12:
X: {0: &#39_&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 0<br/>
X: {0: &#39█&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 1<br/>
X: {0: &#39█&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 2<br/>
X: {0: &#39█&#39, 1: &#39█&#39, 2: &#39█&#39, 3: &#39█&#39, 4: &#39█&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 3<br/>
X: {0: &#39_&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 4<br/>
X: {0: &#39_&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 5<br/>
X: {0: &#39_&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39█&#39, 7: &#39_&#39} Y: 6<br/>
X: {0: &#39_&#39, 1: &#39_&#39, 2: &#39_&#39, 3: &#39_&#39, 4: &#39_&#39, 5: &#39_&#39, 6: &#39_&#39, 7: &#39@&#39} Y: 7<br/></font></pre>

##### Explanation of A*:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;An A* implementation attempt in Python. For my A* implementation I chose to
use heapq, a minimum binary heap.* Which can be used as a priority queue by
placing elements into the heap lead by the given elements 'F score.'* As the
algorithm executes, elements are looped over scanning for neighbors of the
current vertex/node. The current node is added to the closedset after it's
neighbors have been scanned resembling the way that humans view an area as they
decide how to walk to a specific location. This is why A*, which was invented so
that a robot could navigate space, is often used in video games for mob AI.* The
closedset is a set of coordinates, whose values have already been calculated.)
They are placed into the min heap which swaps elements until the neighbor, now
an element in the min heap, with the lowest F score becomes the 0th element in
the min heap. With each loop of the algorithm a new current vertex/node is
popped of the priority queue from the top, the 0th element. The process of
scanning nodes, which some call a "frontier", in the openset happens repeatedly
while the algorithm keeps track of where which vertexes came from forming the
path.  After the goal vertex is found the algorithm returns a list by
reconstructing the path from where each vertex came from starting with the goal,
which was just found.* Provided good implementation of the algorithm, an optimal
path and often the most optimal path can be found in the reversed order of the
path returned from counting backwards from the current to the starting vertex.

##### Summary of my implementation:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I mostly followed the along to a video of Sebastian Lague writing the
algorithm in C# for Unity, the explaination and psuedocode therein was useful. I
also had to get more familiar with coordinates which 3D modeling and programming
my 2D game for Matt Ollis's games course challenged me to learn. I also followed
along to a few other videos, like Computerphile explaination of A* which doesn't
exactly use the best explaination for reasons I'll explain in the weaknesses
section. Nor was Coding Train quite the best way to implement A* because the
programmer from the video did not use a binary heap. They did however use a
class for individual nodes where I used a class containing a dictionary
representation of the graph. Searching with a min binary heap is O(1) only if
it's the 0th or top.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A* struggles with breaking ties between vertexes with the same F score. What
occasionally happens, like in step #6 for the output of this program (if my
improved heuristic is not used), the calculated F score between two points is
the same, but they may not be heading in the right direction. To prioritize
vertexes with the least difference in terms of direction I simply subtracted one
unit vector from another, and subracted the sum of that expression from the F
score.

##### Weaknesses to A*:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Computerphile video I watched used a graph, which was not a grid.  In
the case of using A* to solve a grid, it won't be the most efficient algorithm
for doing so. A* does not differentiate between obstacles or non-existant
vertexes and so they effectively don't exist to the algorithm because they are
ignored. So if a graph is solved using A* star, where the graph itself is
ungridlike (shape) it would be similar in effect to inputting a grid to A* that
contains lots of obstacles. If this is true, it is likely also true that A* is
also most efficient in the case that the graph has many connected nodes
particularly in the center. With the right heuristic, A* can find diagonal
routes from a point a to point b very efficiently if the route is open. There
are also issues with A* picking non-optimal routes, but I fixed that.

##### Sources:

- Python Software Foundation. Heap queue algorithm.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://docs.python.org/2/library/heapq.html

- Wikipedia. A* search algorithm. Description.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://en.wikipedia.org/wiki/A*_algorithm#Description

- Silva, Porfirlo. Shakey.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://www.youtube.com/watch?v=qXdn6ynwpiI

- RedBlob Games. Implementation of A*.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://www.redblobgames.com/pathfinding/a-star/implementation.html

- Lague, Sebastian. A* Pathfinding (E01: algorithm explaination).<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://www.youtube.com/watch?v=-L-WgKMFuhE&feature=youtu.be&list=PLFt_AvWsXl0cq5Umv3pMC9SPnKjfp9eGW&t=131

- Computerphile. A* (A Star) Search Algorithm.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://www.youtube.com/watch?v=ySN5Wnu88nE&t=216s

- Coding Train. Coding Challenge 51.1: A* Pathfinding Algorithm - Part 1.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://www.youtube.com/watch?v=aKYlikFAV4k&t=1535s
