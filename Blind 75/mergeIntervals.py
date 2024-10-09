# Merge Intervals
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# You may return the answer in any order.

# Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

# Example 1:

# Input: intervals = [[1,3],[1,5],[6,7]]

# Output: [[1,5],[6,7]]
# Example 2:

# Input: intervals = [[1,2],[2,3]]

# Output: [[1,3]]
# Constraints:

# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= start <= end <= 1000
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])        
        result = []
        length = len(intervals)
        i = 0
        while i < length:
          print(i)
          new_start = intervals[i][0]
          new_end = intervals[i][1]
          print("Main:", new_start, new_end)
          i += 1
        # Merge any overlapping intervals to the one 'newInterval'
          while i < length:
            print(i)
            interval = intervals[i]
            interval_start = interval[0]
            interval_end = interval[1]
            print(interval_start, interval_end)
            if interval_start <= new_end:
              if new_start > interval_end:
                i += 1
                continue
              if new_start > interval_start:
                new_start = interval_start
              if new_end < interval_end:
                new_end = interval_end
            else:
                break
            i += 1
        # Add either the 'newInterval' or
        # its union with any overlapping intervals
          result.append([new_start, new_end])
        # Add either the 'newInterval' or
        # its union with any overlapping intervals
        # result.append([new_start, new_end])
        return result

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]
        length = len(intervals)
        for i in range(1, length):
          interval = intervals[i]
          interval_start = interval[0]
          interval_end = interval[1]
          results_end = result[-1][1]
          if results_end >= interval_start:
            if results_end < interval_end:
              # Merge
              result[-1][1] = interval_end
          else: # The interval comes after
            result.append(interval)
        return result
    
    def merge4(self, intervals: List[List[int]]) -> List[List[int]]:
      intervals.sort(key = lambda x: x[0])
      result = [intervals[0]]
      for interval_start, interval_end in intervals[1:]:
        results_end = result[-1][1]
        if results_end >= interval_start:
          if results_end < interval_end:
            # Merge
            result[-1][1] = interval_end
        else: # The interval comes after
          result.append([interval_start, interval_end])
      return result   
      