# Insert New Interval
# You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

# You are given another interval newInterval = [start, end].

# Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

# Return intervals after adding newInterval.

# Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

# Example 1:

# Input: intervals = [[1,3],[4,6]], newInterval = [2,5]

# Output: [[1,6]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]

# Output: [[1,2],[3,5],[6,7],[9,10]]
# Constraints:

# 0 <= intervals.length <= 1000
# newInterval.length == intervals[i].length == 2
# 0 <= start <= end <= 1000
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        interval_i = len(intervals) - 1
        while interval_i >= 0:
          interval = intervals[interval_i]
          start_i = interval[0]
          end_i = interval[1]
          if new_start > end_i:
            intervals.insert(interval_i + 1, [new_start, new_end])
            return intervals
          if new_end < start_i:
            if interval_i == 0:
                break
            else:
                interval_i -= 1
                continue
          if new_start > start_i:
            new_start = start_i
          if new_end < end_i:
            new_end = end_i
          intervals.pop(interval_i)
          interval_i -= 1
        intervals.insert(0, [new_start, new_end])
        return intervals
      
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        new_start = newInterval[0]
        new_end = newInterval[1]
        length = len(intervals)
        i = 0
        while i < length:
            interval_end = intervals[i][1]
        # Add all intervals that come before the 'newInterval'
            if interval_end < new_start:
              result.append(intervals[i])
              i += 1
              continue
        # Merge any overlapping intervals to the one 'newInterval'
            interval_start = intervals[i][0]
            if interval_start <= new_end:
              if new_start > interval_start:
                new_start = interval_start
              if new_end < interval_end:
                new_end = interval_end
              i += 1
              continue
        # Add either the 'newInterval' or
        # its union with any overlapping intervals
            result.append([new_start, new_end])
        # Add all the rest of the intervals
            result.extend(intervals[i:])
            return result
    # Add either the 'newInterval' or
    # its union with any overlapping intervals
        result.append([new_start, new_end])
        return result