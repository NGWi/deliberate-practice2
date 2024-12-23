"""
400 point Q:
Sometimes when you wash your clothes <strong>a sock disappears</strong>! <br><br></span><span class="question-statement">Now you are in front of your washing machine and you empty it. While emptying you want to know if you have any lost socks and which ones they are.
<strong>Line 1:</strong> <var>n</var> the number of clothes and underwear in the washing machine.<br><strong>Next <var>n</var> lines:</strong> <var>clothes type</var> <var>clothes size</var> <var>clothes color</var> a string, an int, and a string.<br><br>Socks have the <const>sock</const> clothes type.<br>Pants have the <const>pants</const> clothes type.<br>T-Shirts have the <const>t-shirt</const> clothes type.<br>And so on...<br><br>Two socks form a pair if they are if they have the same <var>clothes type</var>, <var>clothes size</var>, and <var>clothes color</var>.<br><br>Any sock coming out of the washing machine that is not part of a pair indicates that you have lost that other sock.
"""
from calendar import c
import sys
import math

socks = set()
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    inputs = input().split()
    clothes_type = inputs[0]
    clothes_size = int(inputs[1])
    clothes_color = inputs[2]
    # print(f"{clothes_type} {clothes_size} {clothes_color}")

    if clothes_type == "sock":
        if (clothes_size, clothes_color) in socks:
            socks.remove((clothes_size, clothes_color))
        else:
            socks.add((clothes_size, clothes_color))
        
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(len(socks))
sorted_socks = list(sorted(socks))
if len(socks) > 0:
    for sock in sorted_socks:
        print(f"{sock[0]} {sock[1]}")


"""
200 point Q:
You are given a list of characters, all wanted for their heinous crimes. Your job is to determine how many criminal letters are in each given string.
"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
w = set(input())
n = int(input())
matches = [None] * n
for i in range(n):
    area = input()
    matches[i] = sum(c in w for c in area)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for match in matches:
    print(match)

"""
100 point Q:
Your program must decrypt a text encrypted with the Atbash cipher -- a simple substitution
    cipher.<br><br>It consists in substituting <span class="const">a</span> (the first letter) for <span class="const">z</span> (the last), <span class="const">b</span> (the second) for <span class="const">y</span> (one
    before last), and so on, reversing the alphabet.
"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

word = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
cipher = {a: b for a, b in zip(letters, reversed(letters))}
deciphered = ""
for letter in word:
    deciphered += cipher[letter]

print(deciphered)


"""
99 point Q:
The goal is to print the middle element from an array of strings.<br><br>If the array length is an even number, you must print the concatenation of the two centermost elements.<br><br>For example, for the array <const>I, LOVE, YOU</const> you should output the string <const>LOVE</const>.<br>For the array <const>1, 4, potato, 6</const> you should output the string <const>4potato</const>.
"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
s_arr = s.split(" ")
s_len = len(s_arr)
mid = s_len // 2
if s_len % 2 == 1:
    print(s_arr[mid])
else:
    print(s_arr[mid - 1] + s_arr[mid])

"""
100 point Q:
A pangram is a sentence that uses every letter of the alphabet <code>a-z</code> at least once independently of case.<br><br>Your program must indicate whether the given string is a pangram or not.
"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] # Should have written something like this in the other question.
letters_in_s = set()
for letter in s.lower():
    letters_in_s.add(letter)

for letter in letters:
    if letter not in letters_in_s:
        print("false")
        break
else:
    print("true")

