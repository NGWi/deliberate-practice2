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
