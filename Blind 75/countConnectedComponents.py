# # Count Connected Components
# Solved 
# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

# The nodes are numbered from 0 to n - 1.

# Return the total number of connected components in that graph.

# Example 1:

# Input:
# n=3
# edges=[[0,1], [0,2]]

# Output:
# 1
# Example 2:

# Input:
# n=6
# edges=[[0,1], [1,2], [2,3], [4,5]]

# Output:
# 2
# Constraints:

# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1) / 2

class Solution:
    def mergeComponents(self, node: int, otherNode: int, connectedNodes: hash) -> bool:
        """Checks the connected nodes of each node to see if the two nodes are part of the same component. If they are not, it merges their connected nodes and returns True."""
        thisNodesConnections = connectedNodes.get(node, {node})
        otherNodesConnections = connectedNodes.get(otherNode, {otherNode})
        if otherNode not in thisNodesConnections and node not in otherNodesConnections:
            mergedConnections = thisNodesConnections | otherNodesConnections
            connectedNodes[node] = connectedNodes[otherNode] = mergedConnections
            print(connectedNodes)
            return True

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        connectedNodes = {}
        for edge in edges:
            start = edge[0]
            end = edge[1]
            print(start, end)
            if self.mergeComponents(start, end, connectedNodes):
                print("merged")
                components -= 1
            print(components)
        return components
