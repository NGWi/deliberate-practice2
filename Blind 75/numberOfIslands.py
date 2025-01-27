from typing import List
class Solution:
    """ Crashes LeetCode and NeetCode drivers.
    def __init__(self):
            self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            self.island_n = 1
    """
        
    def prop(self, row_n, cell_n, cell):
        print(row_n, cell_n, "(", cell, ")")
        if cell == "1":
            self.new_island = True
            self.grid[row_n][cell_n] = "0"
            for direction in self.directions:
                x = row_n + direction[0]
                y = cell_n + direction[1]
                if x < self.rows and x >= 0 and y < self.cols and y >= 0:
                    print(row_n, cell_n, "(", cell, ")", "=>", x, y)
                    self.prop(x, y, self.grid[x][y])
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.island_n = 1
        self.new_island = False
        for row_n, row in enumerate(grid):
            for cell_n, cell in enumerate(row):
                print("Next cell")
                self.prop(row_n, cell_n, cell)
                if self.new_island:
                    self.island_n += 1
                    self.new_island = False
        return self.island_n - 1

# Test case 1:
grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
# Output: 1
print(Solution().numIslands(grid))

print("-" * 10)
# Test case 2:
grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
# Output: 4
print(Solution().numIslands(grid))