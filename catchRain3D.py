"""
Given an m x n integer matrix heightMap representing the height of each unit 
cell in a 2D elevation map, return the volume of water it can trap after raining.

Example 1:
Input: heightMap = [
[1,4,3,1,3,2],
[3,2,1,3,2,4],
[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.

Example 2:
Input: heightMap = [
[3,3,3,3,3],
[3,2,2,2,3],
[3,2,1,2,3],
[3,2,2,2,3],
[3,3,3,3,3]]
Output: 10

RiverCase: heightMap = [
[12,13, 1,12],
[13, 4,13,12],
[13, 8,10,12],
[12,13,12,12],
[13,13,13,13]]
Output: 14

Constraints:
m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
"""
from typing import List


class Solution:
    # First solution O(n^2) in worst case (8.4-8.7 ms, 45.2 - 45.3 MB):
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows = len(heightMap)
        cols = len(heightMap[0])
        max_x = rows - 1
        max_y = cols - 1
        memo = []
        edge_drainage = [0 for cell in range(cols)]
        memo.append(edge_drainage)
        for row_i in range(1, rows - 1):
            mid_drainage = [0]
            center_drainage = [2 * 10**4 + 1 for col_i in range(1, cols - 1)]
            mid_drainage.extend(center_drainage)
            mid_drainage.append(0)

            memo.append(mid_drainage)
        memo.append(edge_drainage)
        for row in memo: print(row)

        def limit_adjacent(starting_x: int, starting_y: int) -> None:
            """
            Alters memo.
            Also reads max_x and max_y.
            """
            h = heightMap[starting_x][starting_y]
            limit = memo[starting_x][starting_y]
            new_limit = max(h, limit)
            adjacent_cells = []
            if starting_x > 0:
                adjacent_cells.append([starting_x - 1, starting_y])
            if starting_x < max_x:
                adjacent_cells.append([starting_x + 1, starting_y])
            if starting_y > 0:
                adjacent_cells.append([starting_x, starting_y - 1])
            if starting_y < max_y:
                adjacent_cells.append([starting_x, starting_y + 1])
            for cell in adjacent_cells:
                cell_x = cell[0]
                cell_y = cell[1]
                if memo[cell_x][cell_y] > new_limit:
                    memo[cell_x][cell_y] = new_limit
                    limit_adjacent(cell_x, cell_y)

        for y in range(1, max_y):
            limit_adjacent(0, y)
            limit_adjacent(max_x, y)
        for x in range(1, max_x):
            limit_adjacent(x, 0)
            limit_adjacent(x, max_y)

        for row in memo: print(row)

        total_water = 0
        for row_hs, row_ds in zip(heightMap, memo):
            for height, drainage in zip(row_hs, row_ds):
                if drainage > height:
                    water = drainage - height
                    total_water += water

        return total_water
    
    # Second solution, O(n log n) (8 ms, 45.6-45.7 MB):
    def trapRainWater2(self, heightMap: List[List[int]]) -> int:
        rows = len(heightMap)
        cols = len(heightMap[0])
        max_x = rows - 1
        max_y = cols - 1
        memo = []
        edge_drainage = [0 for cell in range(cols)]
        memo.append(edge_drainage)
        for row_i in range(1, rows - 1):
            mid_drainage = [0]
            center_drainage = [2 * 10**4 + 1 for col_i in range(1, cols - 1)]
            mid_drainage.extend(center_drainage)
            mid_drainage.append(0)

            memo.append(mid_drainage)
        memo.append(edge_drainage)
        for row in memo: print(row)

        def limit_adjacent(starting_x: int, starting_y: int, h: int) -> None:
            """
            Alters memo and processed.
            Also reads max_x and max_y.
            """
            processed.add((starting_x, starting_y))
            limit = memo[starting_x][starting_y]
            new_limit = max(h, limit)
            adjacent_cells = []
            if starting_x > 0:
                adjacent_cells.append([starting_x - 1, starting_y])
            if starting_x < max_x:
                adjacent_cells.append([starting_x + 1, starting_y])
            if starting_y > 0:
                adjacent_cells.append([starting_x, starting_y - 1])
            if starting_y < max_y:
                adjacent_cells.append([starting_x, starting_y + 1])
            for cell in adjacent_cells:
                cell_x = cell[0]
                cell_y = cell[1]
                if memo[cell_x][cell_y] > new_limit:
                    memo[cell_x][cell_y] = new_limit
                    if (cell_x, cell_y) not in processed:
                        h = heightMap[cell_x][cell_y]
                        limit_adjacent(cell_x, cell_y, h)

        indexedBorders = []
        for y in range(1, max_y):
            h = heightMap[0][y]
            indexedBorders.append([h, 0, y])
            h = heightMap[max_x][y]
            indexedBorders.append([h, max_x, y])
        for x in range(1, max_x):
            h = heightMap[x][0]
            indexedBorders.append([h, x, 0])
            h = heightMap[x][max_y]
            indexedBorders.append([h, x, max_y])
        sortedBorders = sorted(indexedBorders, key=lambda x: x[0])

        processed = set()
        for h, x, y in sortedBorders:
            limit_adjacent(x, y, h)

        for row in memo: print(row)

        total_water = 0
        for row_hs, row_ds in zip(heightMap, memo):
            for height, drainage in zip(row_hs, row_ds):
                if drainage > height:
                    water = drainage - height
                    total_water += water

        return total_water
