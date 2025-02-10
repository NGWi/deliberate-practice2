"""Find the longest shortest path between two nodes in a graph.
If the question would state that it's acyclical, then it may be more efficient to
build a list of Djikstra distances for each leaf in the graph to every other node,
including the other leafs."""
"""See also https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem"""

def build_graph(number_edges, g_from, g_to):
    graph = {}
    for i in range(number_edges):
        if g_from[i] not in graph:
            graph[g_from[i]] = [g_to[i]]
        else:
            graph[g_from[i]].append(g_to[i])
        if g_to[i] not in graph:
            graph[g_to[i]] = [g_from[i]]
        else:
            graph[g_to[i]].append(g_from[i])
    return graph


def bfs_with_memo(graph, start): 
    """Because the uestion didn't state that the graph is acyclical,
    we need to ensure we aren't coming around to a node more than once."""
    visited = {start}
    layer = [start]
    distance = 0

    while layer:  # Could work with while True because it returns on empty layer
        next_layer = []
        for node in layer:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_layer.append(neighbor)
        distance += 1
        if len(next_layer):
            layer = next_layer
        else:
            return layer, distance


def find_furthest_nodes(graph):
    # First BFS to find the furthest nodes from an arbitrary node
    furthest_nodes_from_start, _ = bfs_with_memo(graph, 1)
    # Second BFS from one of the furthest nodes found
    one_side, _ = bfs_with_memo(graph, furthest_nodes_from_start[0]) 
    # Third BFS to cover if the furthest node is on the same branch as the above starting node
    other_side, max_distance = bfs_with_memo(graph, one_side[0])

    return one_side, other_side, max_distance

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

nodes, distance = find_furthest_nodes(graph)
print(f"The furthest nodes are: {nodes} with a distance of {distance}.")