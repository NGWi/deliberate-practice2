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
              left = mid + 1  # +1 is to avoid getting stuck always 1 less than right because of the rounding down
          else:
              right = mid
      return left
      
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text2_indices = []
        comparison = {char: [] for char in set(text2)}
        for idx, char in enumerate(text2):
          comparison[char].append(idx)
        length = 0
        for char in text1:
          print(char)
          if char in comparison:
            indices = comparison[char]
            print("Comparing:",indices)
            temp_indices = text2_indices.copy()
            last_placement = None
            for j in indices:
              print(text2_indices, j)
              if not text2_indices or j > text2_indices[-1]:
                print("Yay!", j)
                temp_indices.append(j)
                length += 1
                break
              else:
                placement = self.binaryPlacement(text2_indices, length, j)
                if last_placement == None or placement > last_placement:
                  print("Last placement", last_placement, "Replacing", placement)
                  temp_indices[placement] = j
                last_placement = placement
              print(temp_indices)
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
# azope/v
