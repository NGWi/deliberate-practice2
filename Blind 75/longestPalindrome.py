# Longest Palindromic Substring
# Given a string s, return the longest substring of s that is a palindrome.

# A palindrome is a string that reads the same forward and backward.

# If there are multiple palindromic substrings that have the same length, return any one of them.

# Example 1:

# Input: s = "ababd"

# Output: "bab"
# Explanation: Both "aba" and "bab" are valid answers.

# Example 2:

# Input: s = "abbc"

# Output: "bb"
# Constraints:

# 1 <= s.length <= 1000
# s contains only digits and English letters.
class Solution:
    def expansionLoop(self, s: str, pointer_a: int, pointer_b: int, last_i: int):
        while pointer_a >= 1 and pointer_b < last_i:
          if s[pointer_a - 1] == s[pointer_b + 1]:
            pointer_a -= 1
            pointer_b += 1
          else:
            break
        return pointer_a, pointer_b
          
    def longestPalindrome(self, s: str) -> str:
        longest_length = 0
        longest_range = [0, 0]  # A single letter is also a palindrome, and this will avoid a null pointer error when we start "offset"ting
        length = len(s)
        for pointer_a in range(length - 1):
            char_a = s[pointer_a]
            for offset in [1, 2]: # If we're at the central match of a palindrome, the match will be either one or two letters ahead. It may match both, but only one of those matches will centered. So we have to check both.
                if pointer_a + offset < length and char_a == s[pointer_a + offset]:
                    start, end = self.expansionLoop(s, pointer_a, pointer_a + offset, length - 1)
                    new_length = 1 + end - start
                    if new_length > longest_length:
                        longest_length = new_length
                        longest_range = [start, end]
        
        return s[longest_range[0]:(longest_range[1] + 1)]