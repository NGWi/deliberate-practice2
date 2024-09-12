class Solution:
    def forbidConnections(self, node: int, otherNode: int, nodeSet: set) -> bool:
        """ Checks if both nodes are already in the set, returns False if it is, and adds whichever one's missing to the set if it's not."""
        if node in nodeSet and otherNode in nodeSet:
            return False
        nodeSet.update([node, otherNode])


    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges): # Catches orphaned nodes, and loops in O(1) if they are not balanced by orphaned nodes
            return False

        nodeSet = set()
        for edge in edges:
            start = edge[0]
            end = edge[1]
            if self.forbidConnections(start, end, nodeSet) == False: 
                return False           
              
        return True
