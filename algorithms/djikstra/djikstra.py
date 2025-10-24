import heapq

graph = {
    "A": {"B": 2, "C": 1},
    "B": {"D": 5},
    "C": {"D": 1},
    "D": {}
}


def djikstra(graph, start):
    # Heap will store the distance that takes to reach certain node
    min_heap = [(0, start)]

    # Initialize a dict to store the distances values, initialy with inf, to search for the smallest value after
    distances = {node : float("inf") for node in graph}

    # We can already set the initial distance as zero
    distances[start] = 0

    while min_heap:
        # BFS logic
        min_distance, curr_node = heapq.heappop(min_heap)

        # Optimize the code by checking if we already found a better distance for the curr_node
        if min_distance > distances[curr_node]:
            continue

        for neighbor, distance in graph[curr_node].items():
            # Define the new distance between neighbor passing by the curr node
            new_distance = min_distance + distance
            
            # Only update distance and add to the heap if the new_distance is smaller than the existent neighbor distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbor))

    return distances


print(djikstra(graph, "A"))