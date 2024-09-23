## Decode Ways
# A string consisting of uppercase english characters can be encoded to a number using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:

# "JAB" with the grouping (10 1 2)
# "JL" with the grouping (10 12)
# The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

# Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.

# Example 1:

# Input: s = "12"

# Output: 2

# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: s = "01"

# Output: 0
# Explanation: "01" cannot be decoded because "01" cannot be mapped into a letter.

# Constraints:

# 1 <= s.length <= 100
# s consists of digits

class Solution:
    def validateString(self, string: str) -> bool:
        length = len(string)
        last_i = length - 1
        for i in range(length):
            if string[i] == "0" and \
            (i == 0 or string[i - 1] > "2" or (i < last_i and string[i + 1] == "0")):
                return False
        return True

    def countWays(self, string: str) -> int:
        a, b , c = 1, 1, 1
        last_double = len(string) - 1
        last_doubles_i = last_double - 1
        for i in range(last_double):
            two_digit = string[i:i+2]
            a, b = b, c
            if ("11" <= two_digit <= "19" or "21" <= two_digit <= "26") \
            and (i == last_doubles_i or string[i + 2] != "0"):
                c += a
        return c
              
      
    def numDecodings(self, string: str) -> int:
      if self.validateString(string) == False:
        return 0
      else:
        return self.countWays(string)
