"""
Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.

Example 1:
Input: adjList = [[2],[1,3],[2]]

Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].

Example 2:
Input: adjList = [[]]

Output: [[]]
Explanation: The graph has one node with no neighbors.

Example 3:
Input: adjList = []

Output: []
Explanation: The graph is empty.

Constraints:

0 <= The number of nodes in the graph <= 100.
1 <= Node.val <= 100
There are no duplicate edges and no self-loops in the graph.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from calendar import c
from typing import Optional
class Solution:
    def nodepath(self, node):
        copied_node = self.match_ups[node]
        self.match_ups[node] = copied_node
        for neigh in node.neighbors:
            copied_neigh = Node()
            if neigh not in self.match_ups: 
                copied_neigh = Node(neigh.val)
                self.match_ups[neigh] = copied_neigh
            else:
                copied_neigh = self.match_ups[neigh]
            copied_node.neighbors.append(copied_neigh)
            if neigh not in self.visited:
                self.to_visit.append(neigh)
        print("Copied.  ", copied_node.val, [n.val for n in copied_node.neighbors])
        if node.val == 1:
            self.first_node = copied_node

    def get_copied_nodes(self):
        if not self.first_node:
            return []
        visited = set()
        to_visit = [self.first_node]
        result = []
        while to_visit:
            node = to_visit.pop()
            if node not in visited:
                visited.add(node)
                result.append([n.val for n in node.neighbors])
                to_visit.extend(node.neighbors)
        return result

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            print("Empty")
            return node
        self.match_ups = {node: Node(node.val)}
        self.to_visit = [node] 
        self.visited = set()
        self.first_node = Node()
        while self.to_visit:
            start = self.to_visit.pop()
            self.visited.add(start)
            print("Visiting:", start.val, [n.val for n in start.neighbors])
            self.nodepath(start)
            print("Copied nodes:", self.get_copied_nodes())

        print("First node:", self.first_node.val, [n.val for n in self.first_node.neighbors])
        return self.first_node