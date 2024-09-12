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
    def addLetterOrder(self, letter, other, lowerLetterHash, higherLetterHash):
        lowerLetterHash[letter] = (lowerLetterHash.get(letter, set()) |
                                   {other} 
                                #    | lowerLetterHash.get(other, set())
                                )
        higherLetterHash[other] = (higherLetterHash.get(other, set()) |
                                   {letter} 
                                #    | higherLetterHash.get(letter, set())
                                )

    def compareLetters(self, words: List[str], lowerLetterHash, higherLetterHash):
        index = 0
        while index < len(words) - 1:
            word_a = words[index]
            word_b = words[index + 1]
            # print(word_a, word_b)
            l_index = 0
            while l_index < len(word_a) and l_index < len(word_b):
                letter = word_a[l_index]
                other = word_b[l_index]
                # print(letter, other)
                if letter != other:
                    # print(letter, other)
                    self.addLetterOrder(letter, other, lowerLetterHash, higherLetterHash)
                    # print(lowerLetterHash, higherLetterHash)
                    break
                l_index += 1
            index += 1
    def mergeSets(self, letterHash):
        for letter in list(letterHash.keys()):
                mergedSet = set()
                to_process = [letter]
                while to_process:
                    current = to_process.pop()
                    if current not in letterHash:
                        letterHash[current] = set()
                    for other in letterHash.get(current, set()): # will automatically have an empty set because of the previous line, so I canjust do .get(current)
                        if other not in mergedSet:
                            mergedSet.add(other)
                            to_process.append(other)
                letterHash[letter] = mergedSet
    def validateHash(self, letterHash) -> bool:
        for letter in list(letterHash.keys()):
            if letter in letterHash[letter]:
                return False
    def answer(self, letterHash, allLetters) -> str:
        hierarchy = []
        graphed_letters = set(letterHash.keys())
        ordered_letters = sorted(graphed_letters, key=lambda x: len(letterHash[x]))
        wild_cards = list(allLetters - graphed_letters)
        hierarchy += ordered_letters + wild_cards
        return "".join(hierarchy)
    def foreignDictionary(self, words: List[str]) -> str:
        lowerLetterHash = {}
        higherLetterHash = {}
        allLetters = {letter for word in words for letter in word}
        self.compareLetters(words, lowerLetterHash, higherLetterHash)
        # self.mergeSets(lowerLetterHash)
        self.mergeSets(higherLetterHash)
        # print (higherLetterHash)
        # if self.validateHash(lowerLetterHash) == False:
        #     return ""
        if self.validateHash(higherLetterHash) == False:
            return ""
        return self.answer(higherLetterHash, allLetters)