## Dijkstra's Algorithm

Dijkstra's Algorithm is a classic graph traversal algorithm used to find the shortest paths from a single source node to all other nodes in a **weighted graph**.

It is a _greedy_ algorithm because at each step, it selects the unvisited node with the smallest known distance from the source, assuming this local choice will lead to the globally optimal solution.

The primary limitation of Dijkstra's algorithm is that it **does not work correctly if the graph contains negative edge weights**. For such cases, algorithms like the Bellman-Ford must be used.

## Core Implementation Concepts

The modern, efficient implementation of Dijkstra's algorithm uses a **Priority Queue (Min-Heap)** to optimize the selection of the next node to visit.

The essential components are:

1.  **Distances Dictionary (or Array):** A data structure (like a `dict` or array) to store the shortest known distance from the source node to every other node. It is initialized with $\infty$ (`float('inf')`) for all nodes, except for the source node, which starts with a distance of 0.

2.  **Priority Queue (Min-Heap):** The central data structure that makes the algorithm efficient. It stores tuples in the format `(accumulated_distance, node)`. The heap ensures that when we "pop" the next item, it always gives us the node with the smallest accumulated distance from the source that has not yet been definitively processed.

3.  **Relaxation Process:** This is the core logic. When we extract a `current_node` from the min-heap (with its `current_distance`):
    - We iterate over all of its `neighbors`.
    - We calculate the `new_distance` to that neighbor: `new_distance = current_distance + edge_weight(current_node, neighbor)`.
    - We compare: If the `new_distance` is less than the currently recorded distance for that `neighbor` (`distances[neighbor]`), it means we have found a new, shorter path.
    - If so, we update `distances[neighbor] = new_distance` and push `(new_distance, neighbor)` onto the min-heap.

## Complexity

The algorithm's complexity depends directly on the priority queue's implementation.

- **Time Complexity: $O((E + V) \log V)$**

  - Where $V$ is the number of vertices (nodes) and $E$ is the number of edges.
  - Each vertex is inserted into and removed from the min-heap at most once (a $\log V$ operation).
  - Each edge is checked at most once, and each check might result in a heap update (a $\log V$ operation).
  - Therefore, the total complexity is $O(V \log V + E \log V)$, which is commonly simplified to $O((E + V) \log V)$ or $O(E \log V)$ (assuming $E > V$, which is common).

- **Space Complexity: $O(V + E)$**
  - $O(V)$ to store the distances dictionary.
  - $O(E + V)$ to store the graph (in an adjacency list).
  - $O(V)$ to store the items in the min-heap in the worst case.
