"""
You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

Example 1:



Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]

Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
Example 2:

Input: heights = [[1],[1]]

Output: [[0,0],[0,1]]
Constraints:

1 <= heights.length, heights[r].length <= 100
0 <= heights[r][c] <= 1000
"""

from typing import List
from collections import deque
import pdb

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        global width, height, directions
        width = len(heights[0])
        height = len(heights)
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        pacific = [[False for _ in range(width)] for _ in range(height)]
        atlantic = [[False for _ in range(width)] for _ in range(height)]
        pacific_to_check = deque()
        atlantic_to_check = deque()
        for i in range(height):
          pacific[i][0] = True
          atlantic[i][width-1] = True
          pacific_to_check.append((i,0))
          atlantic_to_check.append((i,width-1))
        if width > 1:
          for i in range(width):
            pacific[0][i] = True
            atlantic[height-1][i] = True
            pacific_to_check.append((0,i))
            atlantic_to_check.append((height-1,i))

        
        self.bfs(pacific_to_check, pacific, heights)
        self.bfs(atlantic_to_check, atlantic, heights)
        results = [[r, c] for r in range(height) for c in range(width) if pacific[r][c] and atlantic[r][c]]
        return results
                
    def bfs(self, to_check, ocean, heights):
        while to_check:
          r, c = to_check.popleft()
          for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width and heights[nr][nc] >= heights[r][c] and not ocean[nr][nc]:
              if (nr,nc) not in to_check:
                to_check.append((nr,nc))
                ocean[nr][nc] = True


    def pacificAtlanticSet(self, heights: List[List[int]]) -> List[List[int]]:
        global width, height, directions
        width = len(heights[0])
        height = len(heights)
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        pacific = [[False for _ in range(width)] for _ in range(height)]
        atlantic = [[False for _ in range(width)] for _ in range(height)]
        pacific_to_check = set()
        atlantic_to_check = set()
        for i in range(height):
          pacific[i][0] = True
          atlantic[i][width-1] = True
          pacific_to_check.add((i,0))
          atlantic_to_check.add((i,width-1))
        if width > 1:
          for i in range(width):
            pacific[0][i] = True
            atlantic[height-1][i] = True
            pacific_to_check.add((0,i))
            atlantic_to_check.add((height-1,i))

        
        self.bfs(pacific_to_check, pacific, heights)
        self.bfs(atlantic_to_check, atlantic, heights)
        results = [[r, c] for r in range(height) for c in range(width) if pacific[r][c] and atlantic[r][c]]
        return results
                
    def bfsSet(self, to_check, ocean, heights):
        while to_check:
          next_to_check = set()
          for (r, c) in to_check: 
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < height and 0 <= nc < width and (nr,nc) not in to_check and heights[nr][nc] >= heights[r][c] and not ocean[nr][nc]:
                    next_to_check.add((nr,nc))
                    ocean[nr][nc] = True
          to_check = next_to_check    
          
heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]

print(Solution().pacificAtlantic(heights))
print("*" * 10)
heights=[[1],[1]]
print(Solution().pacificAtlantic(heights))