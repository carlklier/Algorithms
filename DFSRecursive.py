"""
Depth First Search - Recursive

Time Complexity:
O(V+E) - every vertex and every edge will be explored in the worst case.
O(E) may vary between O(1) and O(V^2) depending on how sparse the input graph is.

Space Complexity:
O(v) - In addition to the space required for the graph data structure, you will also need a
data structure to keep track of which nodes have already been discovered.

Considerations:
* A graph can have cycles.
* A graph can have more than one edge between nodes.
* A graph can have self loops.
* A graph can be disconnected
* A graph can be directed or undirected

Applications:
Finding connected compondents in a graph
Topological sorting
Determining if a graph is 2-colorable or bipartite
Finding the bridges in a graph
Finding strongly connected components in a directed graph
Finding biconnected compoents

Notes:
DFS can be implemented recursively or iteratively. 
DFS, however, can get lost in an infinite branch and never make it to a solution node.
A search method is described as being complete if it is guaranteed to find a goal state if one exists. Breadth-first search is complete, but depth-first search is not.


"""

from DataStructures.AdjacencyListUndirected import AdjacencyListUndirected

def DFSRecursive(graph, v, discovered):
  discovered[v] = True
  print(v, end=' ')
  
  for u in graph.adjList[v]:
    if not discovered[u]:
      DFSRecursive(graph, u, discovered)

 
if __name__ == '__main__':
 
    edges = [
        (0, 13), (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # vertex 14 is a single node
    ]
 
    # total number of nodes in the graph (labelled from 0 to 14)
    n = 15
    graph = AdjacencyListUndirected(edges, n)
 
    discovered = [False] * n
 
    # Perform BFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            DFSRecursive(graph, i, discovered)
            print()