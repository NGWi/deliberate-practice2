from typing import List
class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.island_n = 1
        
    def prop(self, row_n, cell_n, cell):
        print(row_n, cell_n, "(", cell, ")")
        if cell == "1":
            self.new_island = True
            self.g[row_n][cell_n] = "0"
            for direction in self.directions:
                x = row_n + direction[0]
                y = cell_n + direction[1]
                if x < self.r and x >= 0 and y < self.c and y >= 0:
                    print(row_n, cell_n, "(", cell, ")", "=>", x, y)
                    self.prop(x, y, self.g[x][y])
        
    def numIslands_propagate(self, grid: List[List[str]]) -> int:
        self.g = grid
        self.r = len(grid)
        self.c = len(grid[0])
        self.new_island = False
        for row_n, row in enumerate(grid):
            for cell_n, cell in enumerate(row):
                print("Next cell")
                self.prop(row_n, cell_n, cell)
                if self.new_island:
                    self.island_n += 1
                    self.new_island = False
        return self.island_n - 1

    def stackify(self, row_n, cell_n, cell):
        print(row_n, cell_n, "(", cell, ")")
        if cell == "1":
            self.g[row_n][cell_n] = "0"
            for direction in self.directions:
                x = row_n + direction[0]
                y = cell_n + direction[1]
                if x < self.r and x >= 0 and y < self.c and y >= 0:
                    print(row_n, cell_n, "(", cell, ")", "=>", x, y)
                    self.stack.append((x, y))
            while self.stack:
                x, y = self.stack.pop()
                self.stackify(x, y, self.g[x][y])

    def numIslands_stackify(self, grid: List[List[str]]) -> int: # Stackify
        if not grid:
            return 0
        self.g = grid
        self.r = len(grid)
        self.c = len(grid[0])
        self.new_island = False
        for row_n, row in enumerate(grid):
            for cell_n, cell in enumerate(row):
                print("Next cell")
                if cell == "1":
                    self.new_island = True
                    self.stack = []
                    self.stackify(row_n, cell_n, cell)
                if self.new_island:
                    self.island_n += 1
                    self.new_island = False

        return self.island_n - 1

    def dfs(self, row_n, cell_n, cell):
        print(row_n, cell_n, "(", cell, ")")
        if cell == "1":
            self.g[row_n][cell_n] = "0"
            for direction in self.directions:
                x = row_n + direction[0]
                y = cell_n + direction[1]
                if x < self.r and x >= 0 and y < self.c and y >= 0:
                    print(row_n, cell_n, "(", cell, ")", "=>", x, y)
                    self.dfs(x, y, self.g[x][y])
        return

    def numIslands(self, grid: List[List[str]]) -> int: # DFS-Style coding
        if not grid:
            return 0
        self.g = grid
        self.r = len(grid)
        self.c = len(grid[0])
        self.island_n = 0
        for row_n, row in enumerate(grid):
            for cell_n, cell in enumerate(row):
                print("Next cell")
                if cell == "1":
                    self.island_n += 1
                    self.dfs(row_n, cell_n, cell)

        return self.island_n
        
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