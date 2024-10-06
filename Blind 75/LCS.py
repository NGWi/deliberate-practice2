# # Longest Common Subsequence
# Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

# A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

# For example, "cat" is a subsequence of "crabt".
# A common subsequence of two strings is a subsequence that exists in both strings.

# Example 1:

# Input: text1 = "cat", text2 = "crabt" 

# Output: 3 
# Explanation: The longest common subsequence is "cat" which has a length of 3.

# Example 2:

# Input: text1 = "abcd", text2 = "abcd"

# Output: 4
# Example 3:

# Input: text1 = "abcd", text2 = "efgh"

# Output: 0
# Constraints:

# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

class Solution:
    def binaryPlacement(self, text2_indices: list, length: int, text2_i: int) -> int:
      """
      Returns the index where char should be inserted in rankings.
      """
      left, right = 0, length
      while left < right:
          mid = (left + right) // 2 # Rounds down to stay within ranking's range.
          if text2_indices[mid] < text2_i:
              left = mid + 1        # +1 is to avoid getting stuck always 1 less than right because of the rounding down
          else:
              right = mid
      return left
      
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text2_indices = []  # Will store the index in text2 of each character that could potentially be part of the LCS
        comparison = {char: [] for char in set(text2)} # Dict for O(1) lookup of each characters indices in text2
        for idx, char in enumerate(text2):
          comparison[char].append(idx)
          
        length = 0          # Current length of best LCS so far, so I can save retrieving it from the list object.
        for char in text1:  
          if char in comparison:
            indices = comparison[char]            # Retrieved indices of the char in text2
            temp_indices = text2_indices.copy()   # Making copy so that the char isn't placed at the tail of a Common Sequence that includes itself from a different index in text2 when it's really from the same index in text1.
            last_placement = None                 # Keeping track of the last place the index from text2 was placed, so it's not replaced with a higher index.
            for j in indices:
              if not text2_indices or j > text2_indices[-1]:
                temp_indices.append(j)
                length += 1
                break
              else:
                placement = self.binaryPlacement(text2_indices, length, j) # O(log m) loop
                if last_placement == None or placement > last_placement: 
                  temp_indices[placement] = j
                last_placement = placement
            text2_indices = temp_indices
        return length
      
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
          text1, text2 = text2, text1
        text2_indices = []  # Will store the index in text2 of each character that could potentially be part of the LCS
        comparison = {char: [] for char in set(text2)} # Dict for O(1) lookup of each characters indices in text2
        for idx, char in enumerate(text2):
          comparison[char].append(idx)
          
        length = 0          # Current length of best LCS so far, so I can save retrieving it from the list object.
        for char in text1:  
          if char in comparison:
            indices = comparison[char]            # Retrieved indices of the char in text2
            temp_indices = text2_indices.copy()   # Making copy so that the char isn't placed at the tail of a Common Sequence that includes itself from a different index in text2 when it's really from the same index in text1.
            last_placement = None                 # Keeping track of the last place the index from text2 was placed, so it's not replaced with a higher index.
            for j in indices:
              if not text2_indices or j > text2_indices[-1]:
                temp_indices.append(j)
                length += 1
                break
              else:
                placement = self.binaryPlacement(text2_indices, length, j) # O(log m) loop
                if last_placement == None or placement > last_placement: 
                  temp_indices[placement] = j
                last_placement = placement
            text2_indices = temp_indices
        return length
      
    def longestCommonSubsequence3(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
          text1, text2 = text2, text1
        text2_indices = []  # Will store the index in text2 of each character that could potentially be part of the LCS
        comparison = {char: [] for char in set(text2)} # Dict for O(1) lookup of each characters indices in text2
        for idx, char in enumerate(text2):
          comparison[char].append(idx)
          
        length = 0          # Current length of best LCS so far, so I can save retrieving it from the list object.
        for char in text1:  
          if char in comparison:
            indices = comparison[char]            # Retrieved indices of the char in text2
            temp_indices = text2_indices.copy()   # Making copy so that the char isn't placed at the tail of a Common Sequence that includes itself from a different index in text2 when it's really from the same index in text1.
            last_placement = None                 # Keeping track of the last place the index from text2 was placed, so it's not replaced with a higher index.
            for j in indices:
              if not text2_indices or j > text2_indices[-1]:
                temp_indices.append(j)
                length += 1
                break
              else:
                placement = self.binaryPlacement(text2_indices, length, j) # O(log m) loop
                if last_placement == None or placement > last_placement: 
                  temp_indices[placement] = j
                last_placement = placement
            text2_indices = temp_indices
        return length
        
solution = Solution()
# print(solution.longestCommonSubsequence("cat", "crabt"))
# print(solution.longestCommonSubsequence("abcd", "abcd"))
# print(solution.longestCommonSubsequence("abcd", "efgh"))
# print(solution.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))
# print(solution.longestCommonSubsequence("abcba", "abcbcba"))
# print(solution.longestCommonSubsequence("papmretkborsrurgtina", "nsnupotstmnkfcfavaxgl"))
# print(solution.longestCommonSubsequence("yzebsbuxmtcfmtodclszgh", "ejevmhcvshclydqrulwbyha")) # 6
# print(solution.longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd")) # 4
print(solution.longestCommonSubsequence("azopevefqpmvkvctwhgnivoxqlwrmfyrslyjqlufgxkponkbgpqtifyhgb", "gdsvqvkjmritatgzspyfwpozuzwpujqfctepatuponctwpejwzmbwzarojo")) # 16

import random
import string
import time
def comparePerf():
    sol = Solution()
    total_time = 0
    total_time2 = 0
    total_time3 = 0
    for i in range(1000):
        text1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 1000)))
        text2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 1000)))
        
        start = time.process_time()
        sol1 = sol.longestCommonSubsequence(text1, text2)
        end = time.process_time()
        total_time += end - start
        
        start = time.process_time()
        sol2 = sol.longestCommonSubsequence2(text1, text2)
        end = time.process_time()
        total_time2 += end - start
        assert sol1 == sol2
        
        start = time.process_time()
        sol3 = sol.longestCommonSubsequence3(text1, text2)
        end = time.process_time()
        total_time3 += end - start
        assert sol1 == sol3
        
    print (f"Average of longestCommonSubsequence took {total_time/1000} seconds to run.")
    print (f"Average of longestCommonSubsequence2 took {total_time2/1000} seconds to run.")
    print (f"Average of longestCommonSubsequence3 took {total_time3/1000} seconds to run.")
comparePerf()

# function2 is app. 0.0001 seconds faster than function1. Forcing the longer one to be the j adds 0.0001 seconds instead!
