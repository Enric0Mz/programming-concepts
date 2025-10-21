import collections

graph = { # Adjacency Matrix
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "e": ["b"],
    "d": ["f"],
    "f": [],
    "z": []
}

def dfs_iterative(graph, source):
    stack = [source]
    seen = set()
    
    while stack:
        curr = stack.pop()
        print(curr)
        seen.add(curr)
        for neighbours in graph[curr]:
            if neighbours not in seen:
                stack.append(neighbours)

print("DFS ITERATIVE")
dfs_iterative(graph, "a")


def dfs_recursive(graph, seen, source):
    print(source)
    seen.add(source)
    for neighbour in graph[source]:
        if neighbour not in seen:
            dfs_recursive(graph, seen, neighbour)

print("DFS RECURSIVE")
dfs_recursive(graph, set(), "a")

def bfs(graph, source):
    queue = collections.deque()
    queue.append(source)
    seen = set()

    while queue:
        curr = queue.popleft()
        print(curr)
        seen.add(curr)
        for neighbour in graph[curr]:
            if neighbour not in seen:
                queue.append(neighbour)


print("BFS")
bfs(graph, "a")

# Checks if source has path to specific item
def has_path(graph, source, item, seen):
    if source == item: return True
    if source in seen: return False
    seen.add(source)

    for neighb in graph[source]:
        if has_path(graph, neighb, item, seen):
            return True
    
    return False


edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]


def convert_edges_into_adj_list(edges: list[list]) -> dict:
    result = collections.defaultdict(list)
    for a, v in edges:
        result[a].append(v)
        result[v].append(a) # Coment this if the edges are not both sides

    return result

edges_graph = convert_edges_into_adj_list(edges)

print(has_path(edges_graph, "l", "k", set()))

teste = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

print("AQUI")
print(dfs_recursive(teste,set(), 0))

