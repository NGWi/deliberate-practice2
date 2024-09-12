# # Valid Tree (https://neetcode.io/problems/valid-tree) from Slack group's archives/C6F5MDB1P/p1725975875991079
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Example 1:

# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

# Output:
# true
# Example 2:

# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

# Output:
# false
# Note:

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
# Constraints:

# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1) / 2


class Solution:
    def forbidConnections(
        self, node: int, otherNode: int, forbiddenHash: dict
    ) -> (
        bool
    ):  # If it could only by used by the validTree function it wouldn't need to be passed the forbiddenHash, but it's always better to be explicit anyways even if its more verbose.
        """Takes a suggested connection, adds ancestor nodes to one of the nodes' entry in the forbiddenHash "database", or returns False if it is an already forbidden connection."""
        forbiddenForThisNode = forbiddenHash.get(node, [])
        if otherNode in forbiddenForThisNode:
            return False
        if otherNode in forbiddenHash:
            forbiddenForThisNode.extend(forbiddenHash[otherNode])

        forbiddenHash[node] = forbiddenForThisNode + [otherNode]  # Need to do otherNode to pass, e.g. n=5, edges=[[0,1],[0,2],[1,2],[3,4]]

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(
            edges
        ):  # Catches orphaned nodes, and loops in O(1) if they are not balanced by orphaned nodes
            return False

        forbiddenHash = {}
        for edge in edges:
            start = edge[0]
            end = edge[1]
            if self.forbidConnections(start, end, forbiddenHash) == False:
                return False
            if (
                self.forbidConnections(end, start, forbiddenHash) == False
            ):  # Need to do both to pass, e.g. n=5, edges=[[0,1],[1,3],[3,0],[2,4]]
                return False

        return True
