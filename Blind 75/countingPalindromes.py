class Solution:
    def expansionLoop(self, s: str, pointer_a: int, pointer_b: int, last_i: int):
        new_pals = 0
        while pointer_a >= 1 and pointer_b < last_i:
          if s[pointer_a - 1] == s[pointer_b + 1]:
            new_pals += 1
            pointer_a -= 1
            pointer_b += 1
          else:
            break
        return new_pals
          
    def countSubstrings(self, s: str) -> str:
        length = len(s)
        total_pals = length # A single letter is also a palindrome.
        for pointer_a in range(length - 1):
            char_a = s[pointer_a]
            for offset in [1, 2]: # If we're at the central match of a palindrome, the match will be either one or two letters ahead. It may match both, but only one of those matches will centered. So we have to check both.
                if pointer_a + offset < length and char_a == s[pointer_a + offset]:
                    total_pals += 1
                    total_pals += self.expansionLoop(s, pointer_a, pointer_a + offset, length - 1)
        
        return total_pals