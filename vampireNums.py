''' 	
Goal
A Vampire number is a number where the digits can be split to equal length factors.

For example:
1260 is a vampire number because it is equal to 21*60 and both 21 and 60 use the same digits as in 1260 (2,1,6, and 0). The length of the two factors must also be equal (length of 21 == length of 60).

Your job is to determine if V is a vampire number by either outputting its two factors (smaller factor first), or output VAN HELSING if the number is not a vampire number.

If the number has more fang pairs (more solutions), use the one with the smallest first factor.

More on vampire numbers:
https://en.wikipedia.org/wiki/Vampire_number
Input
Line 1: An integer V as the potential Vampire Number
Output
Line 1 : Either the two factors in ascending order of the vampire number, or VAN HELSING
Constraints
0 < V < 10^10
Example
Input
1260
Output
21 60
'''
import sys
import math
import itertools

v = int(input())

def is_vampire(n, f1, f2):
    return sorted(str(f1) + str(f2)) == sorted(str(n)) and len(str(f1)) == len(str(f2))

for f1 in range(1, int(math.sqrt(v)) + 1):
    if v % f1 == 0:
        f2 = v // f1
        if is_vampire(v, f1, f2):
            print(f1, f2)
            sys.exit()

print("VAN HELSING")

v = int(input())
for f1 in range(1, int(v**0.5) + 1):
    if v % f1 == 0 and len(str(f1)) == len(str(v))//2 and sorted(str(f1) + str(v//f1)) == sorted(str(v)):
        print(f1, v//f1)
        break
else: print("VAN HELSING")
