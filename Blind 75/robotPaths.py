import math
class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        up_to = [[1] * cols]
        for row in range(1, rows):
            row_arr = [1]
            for col in range(1, cols):
                row_arr.append(up_to[row - 1][col] + row_arr[- 1])
            up_to.append(row_arr)
        return up_to[-1][-1]

    def uniquePathsB(self, rows: int, cols: int) -> int:
        row_arr_a = [1] * cols
        for _row_ in range(1, rows):
            row_arr_b = [1]
            for col in range(1, cols):
                row_arr_b.append(row_arr_a[col] + row_arr_b[- 1])
            row_arr_a = row_arr_b
        return row_arr_a[-1]
    
    def uniquePathsC(self, rows: int, cols: int) -> int:
        row_arr = [1] * cols
        for _row_ in range(1, rows):
            cell = 1
            for col in range(1, cols):
                row_arr[col] += cell
                cell = row_arr[col] 
            print(row_arr)     
        return row_arr[-1]
    
    def uniquePathsD(self, rows: int, cols: int) -> int:
        row_arr = [1] * cols
        cell = 1
        x = 1
        for _row_ in range(1, rows):
          for col in range(x, cols):
              row_arr[col] += cell
              cell = row_arr[col]    
        return row_arr[-1]
    
    
    def uniquePathsM(self, rows:int, cols: int) -> int:
        return math.factorial(rows + cols - 2) // (math.factorial(rows - 1) * math.factorial(cols - 1))
      
    def uniquePathsN(self, rows:int, cols: int) -> int:
        return math.comb(rows + cols - 2, rows - 1)
      
solution = Solution()
example_a = (3, 6)
output = solution.uniquePaths(3, 6)
output = solution.uniquePathsB(3, 6)
output = solution.uniquePathsC(3, 6)
# output = solution.uniquePathsM(3, 6)
assert output == 21

example_b = (3, 3)
output = solution.uniquePaths(3, 3)
output = solution.uniquePathsB(3, 3)
output = solution.uniquePathsC(3, 3)
# output = solution.uniquePathsM(3, 3)
assert output == 6

# Performance Tests:
# import time
# import numpy as np
# import matplotlib.pyplot as plt

# def test_unique_paths():
#     solution = Solution()
#     n = 101
#     mn = range(1, n)
#     uniquePaths_times = np.zeros((n, n))
#     uniquePathsB_times = np.zeros((n, n))
#     uniquePathsC_times = np.zeros((n, n))
#     uniquePathsM_times = np.zeros((n, n))
#     uniquePathsN_times = np.zeros((n, n))

#     for row in mn:
#         print("Row size:", row)
#         for cols in mn:
#             start_time = time.time()
#             solution.uniquePaths(row, cols)
#             end_time = time.time()
#             uniquePaths_times[row-1, cols-1] = (end_time - start_time) / (row * cols)

#             start_time = time.time()
#             solution.uniquePathsB(row, cols)
#             end_time = time.time()
#             uniquePathsB_times[row-1, cols-1] = (end_time - start_time) / (row * cols)
            
#             start_time = time.time()
#             solution.uniquePathsC(row, cols)
#             end_time = time.time()
#             uniquePathsC_times[row-1, cols-1] = (end_time - start_time) / (row * cols)
            
#             start_time = time.time()
#             solution.uniquePathsM(row, cols)
#             end_time = time.time()
#             uniquePathsM_times[row-1, cols-1] = (end_time - start_time) / (row * cols)
            
#             start_time = time.time()
#             solution.uniquePathsN(row, cols)
#             end_time = time.time()
#             uniquePathsN_times[row-1, cols-1] = (end_time - start_time) / (row * cols)

#     print(uniquePathsM_times)
#     print(uniquePathsN_times)
    
#     mean_uniquePaths_time = np.mean(uniquePaths_times, axis=1)
#     mean_uniquePathsB_time = np.mean(uniquePathsB_times, axis=1)    
#     mean_uniquePathsC_time = np.mean(uniquePathsC_times, axis=1)
#     mean_uniquePathsM_time = np.mean(uniquePathsM_times, axis=1)
#     mean_uniquePathsN_time = np.mean(uniquePathsN_times, axis=1)

#     # plt.plot(mean_uniquePaths_time, label='uniquePaths')
#     # plt.plot(mean_uniquePathsB_time, label='uniquePathsB')
#     # plt.plot(mean_uniquePathsC_time, label='uniquePathsC')
#     plt.plot(mean_uniquePathsM_time, label='uniquePathsM')
#     plt.plot(mean_uniquePathsN_time, label='uniquePathsN')
#     plt.xlabel('Rows')
#     plt.ylabel('Mean Time per Cell (seconds)')
#     plt.title('Performance Comparison')
#     plt.legend()
#     plt.show()

# test_unique_paths()
