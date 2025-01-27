class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        island_n = 1
        island_ns = [[0 for c in range(cols)] for r in range(rows)]
        for row_n, row in enumerate(grid):
            for cell_n, cell in enumerate(row):
                def prop(row_n, cell_n, cell):
                    print(row_n, cell_n, cell)
                    if cell == "1" and island_ns[row_n][cell_n] == 0:
                        island_ns[row_n][cell_n] == island_n
                        print(island_n)
                        for direction in directions:
                            x = row_n + direction[0]
                            y = cell_n + direction[1]
                            if x < rows and x >= 0 and y < cols and y >= 0:
                                prop(x, y, grid[x][y])
                print("Next cell")
                prop(row_n, cell_n, cell)
        return island_n - 1