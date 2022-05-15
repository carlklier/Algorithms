"""
Breadth First Search

Complexity:
O(V+E)

Considerations:
* Graph has cycles
* A node has no edges - disconnected graph
* Graph is directed vs undirected

Applications:

"""
from collections import deque

from DataStructures.AdjacencyListUndirected import AdjacencyListUndirected

def BFS(graph, v, discovered):
 
    q = deque()
    discovered[v] = True
    q.append(v)
 
    while q:
 
        v = q.popleft()
        print(v, end=' ')
 
        for u in graph.adjList[v]:
            if not discovered[u]:
                discovered[u] = True
                q.append(u)
 
 
if __name__ == '__main__':
 
    edges = [
        (0, 13), (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # vertex 0, 13, and 14 are single nodes
    ]
 
    # total number of nodes in the graph (labelled from 0 to 14)
    n = 15
    graph = AdjacencyListUndirected(edges, n)
 
    discovered = [False] * n
 
    # Perform BFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            BFS(graph, i, discovered)
            print()