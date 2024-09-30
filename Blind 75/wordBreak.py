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
from typing import List

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
    
    def wordSearch(self, string: str, starting_index: int, last_index: int, length: int, longest_w_len: int, word_dict: List[str]) -> bool | set:
        new_outstanding_indexes = set()
        potential_word = ""
        for i in range(starting_index, min(length, starting_index + longest_w_len + 1)):
            potential_word += string[i]
            if potential_word in word_dict:
                if i == last_index:
                    return True
                new_outstanding_indexes.add(i + 1)
        return new_outstanding_indexes
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      longest_w_len = max(len(word) for word in wordDict)
      wordDict = set(wordDict)
      length = len(s)
      last_index = length - 1
      outstanding_indexes = {0}
      while outstanding_indexes:
        starting_index = outstanding_indexes.pop()
        new_outstanding_indexes = self.wordSearch(s, starting_index, last_index, length, longest_w_len, wordDict)
        if new_outstanding_indexes == True:
          return True
        elif new_outstanding_indexes:
          outstanding_indexes.update(new_outstanding_indexes)
      return False
    
# DP solutions

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      longest_w_len = max(len(word) for word in wordDict)
      wordDict = set(wordDict)
      up_to = [False] * (len(s) + 1) # We will align i in this list with s[i - 1] as follows.
      up_to[0] = True # This is the value for before the first character.
      for i in range(1, len(s) + 1): # This i is aligned with i in the up_to.
          for j in range(max(0, i - longest_w_len), i):  # Potentintial starting characters before the character at s[i]
              if up_to[j] and s[j:i] in wordDict: # That through s[j - 1] it was true and from j through s[i - 1] is another word.
                  up_to[i] = True # We've found a way to break up through s[i - 1] into words...
                  break # so we can move on to trying with s[i].
      return up_to[-1] # Check if we were successful with s["last_index"]
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        longest_w_len = max(len(word) for word in wordDict)
        wordDict = set(wordDict)
        up_to = [True] # This is the value for before the first character. We will align i in this list with s[i - 1] as follows.
        for i in range(1, len(s) + 1): # This i is aligned with i in the up_to.
            last_j = i - 1
            for j in range(max(0, i - longest_w_len), i):  # Potentintial starting characters before the character at s[i]
                if up_to[j] and s[j:i] in wordDict: # That through s[j - 1] it was true and from j through s[i - 1] is another word.
                    up_to.append(True) # We've found a way to break up through s[i - 1] into words...
                    break # so we can move on to trying with s[i].
                if j == last_j:
                    up_to.append(False)
        return up_to[-1] # Check if we were successful with s["last_index"]
      
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      longest_w_len = max(len(word) for word in wordDict)
      wordDict = set(wordDict)
      up_to = [False] * (len(s) + 1) # We will align i in this list with s[i - 1] as follows.
      up_to[0] = True # This is the value for before the first character.
      for i in range(1, len(s) + 1): # This i is aligned with i in the up_to.
          for j in range(i - 1, max(-1, i - longest_w_len - 1) - 1, -1):  # Move backwards through potential starting characters before the character at s[i]
              if up_to[j] and s[j:i] in wordDict: # That through s[j - 1] it was true and from j through s[i - 1] is another word.
                  up_to[i] = True # We've found a way to break up through s[i - 1] into words...
                  break # so we can move on to trying with s[i].
      return up_to[-1] # Check if we were successful with s["last_index"]
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        longest_w_len = max(len(word) for word in wordDict)
        wordDict = set(wordDict)
        up_to = [True] # This is the value for before the first character. We will align i in this list with s[i - 1] as follows.
        for i in range(1, len(s) + 1): # This i is aligned with i in the up_to.
            first_j = max(0, i - longest_w_len)
            for j in range(i - 1, first_j - 1, -1):   # Move backwards through potential starting characters before the character at s[i]
                if up_to[j] and s[j:i] in wordDict: # That through s[j - 1] it was true and from j through s[i - 1] is another word.
                    up_to.append(True) # We've found a way to break up through s[i - 1] into words...
                    break # so we can move on to trying with s[i].
                if j == first_j:
                    up_to.append(False)
        return up_to[-1] # Check if we were successful with s["last_index"]
      
      
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      str_len = len(s)
      longest_w_len = max(len(word) for word in wordDict)
      wordDict = set(wordDict)
      up_to = [0] # Indices where the preceding string evaluated as True
      for i in range(1, str_len + 1):
          first_j = i - longest_w_len # First potential starting character. Will also be limited to 0 in the next line
          for j in up_to[::-1]:       # Move backwards through potential starting characters before the character at s[i]
              if j < first_j: break   # Give up on this i
              if s[j:i] in wordDict:  # That through s[j - 1] it was true and from j through s[i - 1] is another word.
                  up_to.append(i)     # We've found a way to break up through s[i - 1] into words...
                  break               # so we can move on to trying with s[i].
                
      return up_to[-1] == str_len # Check if we were successful with s["last_index"]

    # Memory optimization and time trade-off: remove j that is less than first_j from the list. It will cost reindexing, but we will never retrieve it again. 
    # Also, optionally, if up_to becomes empty, we can immediately return False.
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      str_len = len(s)
      longest_w_len = max(len(word) for word in wordDict)
      wordDict = set(wordDict)
      up_to = [0] # Indices where the preceding string evaluated as True
      for i in range(1, str_len + 1):
          first_j = i - longest_w_len # First potential starting character. Will also be limited to 0 in the next line.
          for j in up_to[::-1]:       # Move backwards through potential starting characters before the character at s[i]
              if j < first_j: 
                  up_to.remove(j)     # Will never have need for it again. <-- MEMORY OPTIMIZATION
                  if not up_to: return False  # <-- Optional. If the last valid j is already out of range, we don't have to bother with the rest of the string.
                  break               # Give up on this i
              if s[j:i] in wordDict:  # That through s[j - 1] it was true and from j through s[i - 1] is another word.
                  up_to.append(i)     # We've found a way to break up through s[i - 1] into words...
                  break               # so we can move on to trying with s[i].
                
      return up_to[-1] == str_len     # Check if we were successful with s["last_index"]. 
      # If you don't use the optional `if not up_to: return False`, then you have to add after `return` `bool(up_to) and` because we could end up with an empty up_to list.
    
    # Most "pure" DP
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      str_len = len(s)
      longest_w_len = max(len(word) for word in wordDict)
      wordDict = set(wordDict)
      up_to = [0] # Indices where the preceding string evaluated as True
      for i in range(1, str_len + 1):
          first_j = i - longest_w_len # First potential starting character. Will also be limited to 0 in the next line.
          for up_to_index, j in enumerate(up_to[::-1]): # Move backwards through potential starting characters before the character at s[i]
              if j <= first_j:            # Will never have need for the earlier ones again.
                  if up_to_index == 0:    # # The enumerable's up_to_index started from 0 and goes up.
                    up_to = []
                  else: 
                    up_to = up_to[-(up_to_index):]  
                  if j < first_j: break       # Give up on this i
              if s[j:i] in wordDict:      # That through s[j - 1] it was true and from j through s[i - 1] is another word.
                  up_to.append(i)         # We've found a way to break up through s[i - 1] into words...
                  break                   # so we can move on to trying with s[i]. 
              if not up_to: return False  # If the last valid j will be out of range, we don't have to bother with the rest of the string.
      return up_to[-1] == str_len         # Check if we were successful with s["last_index"].
    
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
      str_len = len(s)
      longest_w_len = max(len(word) for word in wordDict)
      wordDict = set(wordDict)
      up_to = [0] # Indices where the preceding string evaluated as True
      for i in range(1, str_len + 1):
          earliest_start = i - longest_w_len # First potential starting character. Will also be limited to 0 in the next line.
          j = -1
          last_j = -len(up_to)
          while j >= last_j:                 # Move backwards through potential starting characters before the character at s[i]
              starting_index = up_to[j]
              if starting_index <= earliest_start:      # We will never have need for the earlier ones again. 
                  if j == -1: 
                    up_to = []
                  else: 
                    up_to = up_to[j + 1:]
                  if starting_index == earliest_start: 
                    last_j = j              # So we will break if we don't find a match now.
                  else: break               # Give up on this i
              if s[starting_index:i] in wordDict:      # That through s[starting_index - 1] it was true and from starting_index through s[i - 1] is another word.
                  up_to.append(i)           # We've found a way to break up through s[i - 1] into words...
                  break                     # so we can move on to trying with s[i]. 
              if not up_to: return False    # If the last valid j will be out of range, we don't have to bother with the rest of the string.
              j -= 1
      return up_to[-1] == str_len           # Check if we were successful with s["last_index"].
    

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """Return whether or not s can be broken up into words from wordDict."""
        str_len = len(s)
        longest_w_len = max(len(word) for word in wordDict)
        wordDict = set(wordDict)
        up_to = [0]  # Indices where the preceding string evaluated as True
        for i in range(1, str_len + 1):
          earliest_start = i - longest_w_len
          up_to = self.partialBreak(s, i, earliest_start, up_to, wordDict)
          if not up_to:
                return False
        return up_to[-1] == str_len

    def partialBreak(self, s: str, i: int, earliest_start: int, up_to: List[int], wordDict: set) -> bool:
        """Return whether or not s[:i] can be broken up into words from wordDict."""
        j = -1
        last_j = -len(up_to)
        while j >= last_j:
            starting_index = up_to[j]
            if starting_index <= earliest_start:
                if j == -1:
                    up_to = []
                else:
                    up_to = up_to[j + 1:]
                if starting_index == earliest_start:
                    last_j = j
                else:
                    break
            print(s[starting_index:i])
            if s[starting_index:i] in wordDict:
                up_to.append(i)
                return up_to
            if not up_to:
                break
            j -= 1
        return up_to
      
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
      str_len = len(s)
      unique_word_lengths = list(set(len(word) for word in wordDict))
      longest_w_len = max(unique_word_lengths)
      latest_i = longest_w_len
      wordDict = set(wordDict)
      up_to = {0}              # Indices where the preceding string evaluated as True
      for i in range(1, str_len + 1):
          if i > latest_i: return False                  # If its out of range, we don't have to bother with the rest of the string.
          for j in unique_word_lengths:
              starting_index = i - j
              if starting_index in up_to:
                if s[starting_index:i] in wordDict:      # That through s[starting_index - 1] it was true and from starting_index through s[i - 1] is another word.
                  up_to.add(i)
                  latest_i = i + longest_w_len           # We've found a way to break up through s[i - 1] into words...
                  break                                  # so we can move on to trying with s[i]. 
      return str_len in up_to   # Check if we were successful with s["last_index"].
    
    
import random
import string
import timeit

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def break_down_string(s, word_dict, num_extra_words=0, remove_word=False):
    words = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j] in word_dict]
    if remove_word:
        words.pop(random.randint(0, len(words)-1))
    words.extend([generate_random_string(random.randint(1, 20)) for _ in range(num_extra_words)])
    random.shuffle(words)
    return ' '.join(words)

# # Generate a random string of length 200
# s = generate_random_string(600)

# # Create a dictionary of 100 words
# word_dict = [generate_random_string(random.randint(1, 20)) for _ in range(10000)]

# # Break down the string into a dictionary with some extra random words
# # and remove one of the essential words
# false_example = break_down_string(s, word_dict, num_extra_words=10, remove_word=True)

# def generate_true_example(s, word_dict):
#     words = [word for word in s.split() if word in word_dict]
#     random.shuffle(words)
#     return ' '.join(words)

# # Generate an example that evaluates as true
# true_example = generate_true_example(s, word_dict)

# # Create a Solution instance
# solution = Solution()

# # Time the execution of wordBreak1 and wordBreak2
# print("Testing wordBreak1 and wordBreak2 on false examples...")
# wordBreak1_time = timeit.timeit(lambda: solution.wordBreak1(false_example, word_dict), number=1000)
# wordBreak2_time = timeit.timeit(lambda: solution.wordBreak2(false_example, word_dict), number=1000)
# print("wordBreak1 time:", wordBreak1_time)
# print("wordBreak2 time:", wordBreak2_time)

# print("Testing wordBreak1 and wordBreak2 on true examples...")
# wordBreak1_time = timeit.timeit(lambda: solution.wordBreak1(true_example, word_dict), number=1000)
# wordBreak2_time = timeit.timeit(lambda: solution.wordBreak2(true_example, word_dict), number=1000)
# print("wordBreak1 time:", wordBreak1_time)
# print("wordBreak2 time:", wordBreak2_time)

import random
import string
import timeit

# import pandas as pd
# import numpy as np
# from scipy.signal import savgol_filter
import matplotlib.pyplot as plt

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_random_dictionary(num_words):
    return [generate_random_string(random.randint(1, 20)) for _ in range(num_words)]

def generate_true_example(word_dict):
    s = ''.join(random.choice(word_dict) for _ in range(random.randint(1, 10)))
    return s

def generate_false_example(word_dict):
    s = generate_true_example(word_dict)
    s = s + ''.join(random.choices(string.ascii_lowercase, k=10))
    return s

print("Setting up tests...")
string_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000]
dict_sizes = [100, 500, 1000, 2000, 3000]

wordBreak1_true_times = []
wordBreak2_true_times = []
wordBreak1_false_times = []
wordBreak2_false_times = []
string_dict_sizes = []

for string_size in string_sizes:
    print("String size: ", string_size)
    for dict_size in dict_sizes:
        string_dict_sizes.append(string_size * dict_size)
        word_dict = generate_random_dictionary(dict_size)
        true_s = generate_true_example(word_dict)
        true_s = true_s * (string_size // len(true_s)) + true_s[:string_size % len(true_s)]
        false_s = generate_false_example(word_dict)
        false_s = false_s * (string_size // len(false_s)) + false_s[:string_size % len(false_s)]
        
        solution = Solution()
        
        wordBreak1_true_time = timeit.timeit(lambda: solution.wordBreak1(true_s, word_dict), number=100)
        wordBreak2_true_time = timeit.timeit(lambda: solution.wordBreak2(true_s, word_dict), number=100)
        wordBreak1_false_time = timeit.timeit(lambda: solution.wordBreak1(false_s, word_dict), number=100)
        wordBreak2_false_time = timeit.timeit(lambda: solution.wordBreak2(false_s, word_dict), number=100)
        
        wordBreak1_true_times.append(wordBreak1_true_time)
        wordBreak2_true_times.append(wordBreak2_true_time)
        wordBreak1_false_times.append(wordBreak1_false_time)
        wordBreak2_false_times.append(wordBreak2_false_time)
        
        print("wordBreak1 True Times:", wordBreak1_true_time)
        print("wordBreak2 True Times:", wordBreak2_true_time)
        print("wordBreak1 False Times:", wordBreak1_false_time)
        print("wordBreak2 False Times:", wordBreak2_false_time)

# Conclusions:
# wordBreak1 is faster in most of my test cases, but wordBreak2 is faster in very large dict sizes.

# def iterate_list(lst):
#     for _ in lst:
#         pass

# def iterate_set(s):
#     for _ in s:
#         pass

# # Create a large list and set with 10 million elements
# l = list(range(10**7))
# s = set(range(10**7))

# # Benchmark iteration over the list and set
# list_time = timeit.timeit(lambda: iterate_list(l), number=10)
# set_time = timeit.timeit(lambda: iterate_set(s), number=10)

# print(f"Iterating over the list took {list_time:.2f} seconds")
# print(f"Iterating over the set took {set_time:.2f} seconds")