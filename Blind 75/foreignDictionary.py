# # Foreign Dictionary
# There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

# You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

# Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

# A string a is lexicographically smaller than a string b if either of the following is true:

# The first letter where they differ is smaller in a than in b.
# There is no index i such that a[i] != b[i] and a.length < b.length.
# Example 1:

# Input: ["z","o"]

# Output: "zo"
# Explanation:
# From "z" and "o", we know 'z' < 'o', so return "zo".

# Example 2:

# Input: ["hrn","hrf","er","enn","rfnn"]

# Output: "hernf"
# Explanation:

# from "hrn" and "hrf", we know 'n' < 'f'
# from "hrf" and "er", we know 'h' < 'e'
# from "er" and "enn", we know get 'r' < 'n'
# from "enn" and "rfnn" we know 'e'<'r'
# so one possibile solution is "hernf"
# Constraints:

# The input words will contain characters only from lowercase 'a' to 'z'.
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100


class Solution:
    # def addLetterOrder(self, letter, other, lowerLetterHash, higherLetterHash):
    #     lowerLetterHash[letter] = (lowerLetterHash.get(letter, set()) |
    #                                {other}
    #                             #    | lowerLetterHash.get(other, set())
    #                             )
    #     higherLetterHash[other] = (higherLetterHash.get(other, set()) |
    #                                {letter}
    #                             #    | higherLetterHash.get(letter, set())
    #                             )

    def compareLetters(self, words: List[str], conclusions: dict) -> bool:
        word_i = 0
        last_w_i = len(words) - 1
        while word_i < last_w_i:
            word_a = words[word_i]
            word_b = words[word_i + 1]
            # print(word_a, word_b)
            letter_i = 0
            len_a = len(word_a)
            len_b = len(word_b)
            length = min(len_a, len_b)
            while letter_i < length:
                letter = word_a[letter_i]
                other = word_b[letter_i]
                # print(letter, other)
                if letter != other:
                    # print(letter, other)
                    conclusions[letter] = conclusions.get(letter, set()) | {other}
                    break
                letter_i += 1
            else:
                if len_a > len_b:
                    return False
            word_i += 1

    def inheritConclusions(self, conclusions: dict):
      master_list = list(conclusions.keys())
      for letter in master_list:
          to_process = set(conclusions[letter])
          while to_process:
              children = to_process
              next_row = set()
              for sibling in children:
                  gchildren = conclusions.get(sibling, set())
                  next_row.update(gchildren)
              conclusions[letter].update(next_row)
              for sibling in children:
                if sibling in conclusions:
                  conclusions[sibling].update(next_row)
              to_process -= children
              to_process.update(next_row)

    def validateConclusions(self, conclusions) -> bool:
        for letter in list(conclusions.keys()):
            if letter in conclusions[letter]:
                return False

    def sortLetters(self, letterHash, allLetters) -> str:
        hierarchy = []
        graphed_letters = set(letterHash.keys())
        ordered_letters = sorted(graphed_letters, key=lambda x: len(letterHash[x]), reverse = True)
        wild_cards = list(allLetters - graphed_letters)
        hierarchy += ordered_letters + wild_cards
        return "".join(hierarchy)

    def foreignDictionary(self, words: List[str]) -> str:
        conclusions = {}
        allLetters = {letter for word in words for letter in word}
        if self.compareLetters(words, conclusions) == False:
            return ""
        print(conclusions)
        self.inheritConclusions(conclusions)
        print(conclusions)
        # if self.validateHash(lowerLetterHash) == False:
        #     return ""
        if self.validateConclusions(conclusions) == False:
            return ""
        return self.sortLetters(conclusions, allLetters)
