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
    def compareLetters(self, words: List[str], conclusions: dict) -> bool:
        word_i = 0
        last_word_i = len(words) - 1
        while word_i < last_word_i:
            word_a = words[word_i]
            word_b = words[word_i + 1]
            letter_i = 0
            len_a = len(word_a)
            len_b = len(word_b)
            length = min(len_a, len_b)
            while letter_i < length:
                letter = word_a[letter_i]
                other = word_b[letter_i]
                if letter != other:
                    conclusions[other] = conclusions.get(other, set()) | {letter}
                    break
                letter_i += 1
            else:
                if len_a > len_b:
                    return False
            word_i += 1

    def sortLetters(self, conclusions, allLetters) -> str:
        hierarchy = []
        graphed_letters = set(conclusions.keys())
        wild_cards = allLetters - graphed_letters
        hierarchy += list(wild_cards)
        graphed_letters = list(graphed_letters)
        while len(wild_cards) > 0:
            low_letters = set()
            for letter in graphed_letters:
                if len(conclusions[letter]) > 0:
                    conclusions[letter] -= wild_cards
                    if len(conclusions[letter]) == 0:
                        hierarchy += letter
                        low_letters.add(letter)
            wild_cards = low_letters
        if len(hierarchy) != len(allLetters):
            return False
        return "".join(hierarchy)

    def foreignDictionary(self, words: List[str]) -> str:
        conclusions = {}
        if self.compareLetters(words, conclusions) == False:
            return ""

        allLetters = {letter for word in words for letter in word}
        result = self.sortLetters(conclusions, allLetters)
        if result == False:
            return ""
        return result
