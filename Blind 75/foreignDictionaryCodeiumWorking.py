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


from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Create a graph data structure, where each node is a character in the words list,
        # and the edges represent the relative order of the characters.
        graph = defaultdict(list)
        # Create a dictionary to store the in-degree of each node (character).
        # The in-degree is the number of edges pointing to the node.
        indegree = {char: 0 for word in words for char in word}

        # Iterate over the words list, and for each pair of adjacent words,
        # check if the first letter of the first word is different from the first letter of the second word.
        # If they are different, then add an edge to the graph from the first letter to the second letter.
        # Also, increment the in-degree of the second letter.
        for first_word, second_word in zip(words, words[1:]):
            for a, b in zip(first_word, second_word):
                if a != b:
                    graph[a].append(b)
                    indegree[b] += 1
                    break
            else:  # Check if second word is a prefix of first word
                # If the second word is a prefix of the first word,
                # then the order is invalid, so return an empty string.
                if len(second_word) < len(first_word):
                    return ""

        # Create a queue and add all the nodes with in-degree 0 to the queue.
        # These nodes have no incoming edges, so they must come first in the order.
        queue = deque([char for char in indegree if indegree[char] == 0])
        result = []

        # While the queue is not empty, pop a node from the queue and add it to the result list.
        # Then, for each of the node's neighbors, decrement its in-degree.
        # If the in-degree of a neighbor becomes 0, add it to the queue.
        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If the length of the result list is not equal to the number of nodes in the graph,
        # then that means there are nodes that have not been added to the result list,
        # which means that there are nodes that have not been able to be added to the result list
        # in a valid order, i.e., the order is invalid, so return an empty string.
        if len(result) != len(indegree):
            return ""
        # Otherwise, return the result list as a string.
        return "".join(result)
