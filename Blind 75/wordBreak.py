# # Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of dictionary words.

# You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.

# Example 1:

# Input: s = "neetcode", wordDict = ["neet","code"]

# Output: true
# Explanation: Return true because "neetcode" can be split into "neet" and "code".

# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen","ape"]

# Output: true
# Explanation: Return true because "applepenapple" can be split into "apple", "pen" and "apple". Notice that we can reuse words and also not use all the words.

# Example 3:

# Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

# Output: false
# Constraints:

# 1 <= s.length <= 200
# 1 <= wordDict.length <= 100
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.

class Solution:
    def wordSearch(self, s: str, starting_index: int, last_index: int, length: int, wordDict: List[str]) -> bool | set:
      new_outstanding_indexes = set()
      potential_word = ""
      word = False
      for i in range(starting_index, length):
        char = s[i]
        potential_word += char
        if potential_word in wordDict:
          new_outstanding_indexes.add(i + 1)
          word = True
        else:
          if word == True:
            word = False
        if i == last_index:
          if word == True:
            return True
          else:
            return new_outstanding_indexes
    
    def wordSearch(self, string: str, starting_index: int, last_index: int, length: int, word_dict: List[str]) -> bool | set:
        new_outstanding_indexes = set()
        potential_word = ""
        for i in range(starting_index, length):
            potential_word += string[i]
            if potential_word in word_dict:
                if i == last_index:
                    return True
                new_outstanding_indexes.add(i + 1)
        return new_outstanding_indexes
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      length = len(s)
      last_index = length - 1
      outstanding_indexes = {0}
      while outstanding_indexes:
        starting_index = outstanding_indexes.pop()
        new_outstanding_indexes = self.wordSearch(s, starting_index, last_index, length, wordDict)
        if new_outstanding_indexes == True:
          return True
        elif new_outstanding_indexes:
          outstanding_indexes.update(new_outstanding_indexes)
      return False
    
# DP solution
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      up_to = [False] * (len(s) + 1) # We will align i in this list with s[i - 1] as follows.
      up_to[0] = True # This is the value for before the first character.
      for i in range(1, len(s) + 1): # This i is aligned with i in the up_to.
          for j in range(i):  # All characters before the character at s[i]
              if up_to[j] and s[j:i] in wordDict: # That through s[j - 1] it was true and from j through s[i - 1] is another word.
                  up_to[i] = True # We've found a way to break up through s[i - 1] into words...
                  break # so we can move on to trying with s[i].
      return up_to[-1] # Check if we were successful with s["last_index"]
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        up_to = [True] # This is the value for before the first character. We will align i in this list with s[i - 1] as follows.
        for i in range(1, len(s) + 1): # This i is aligned with i in the up_to.
            last_j = i - 1
            for j in range(i):  # All characters before the character at s[i]
                if up_to[j] and s[j:i] in wordDict: # That through s[j - 1] it was true and from j through s[i - 1] is another word.
                    up_to.append(True) # We've found a way to break up through s[i - 1] into words...
                    break # so we can move on to trying with s[i].
                if j == last_j:
                    up_to.append(False)
        return up_to[-1] # Check if we were successful with s["last_index"]
          