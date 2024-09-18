# Goal
# Its's time to create a big tree!
# For this, use the L system like this:
# (begin with the letter "A")
# if you have an "A", return "AB" (A=>AB)
# if you have "B", return "A" (B=>A)
# -------------------------------------------------------------------------------------------------------------------------------------------
# A --> AB
# B --> A
# -------------------------------------------------------------------------------------------------------------------------------------------
# Input
# an integer n: the number of iterations
# Output
# the tree

# example :
# n=4
# A
# AB <=("AB" from the A)
# ABA <=("AB" from A and "A" from B)
# ABAAB <=("AB" from A, "A" from B, and "AB" from the last A)
# Constraints
# 20>n>0
# and n ∈ ℕ .
# Example
# Input
# 1
# Output
# A

# SuperMuppet (60b):
s=?A
gets.to_i.times{puts s
s=s.chars.map{_1<?B?'AB':?A}*''}

# Mathieu (70b):
r="A"
gets.to_i.times{
puts r
r=r.chars.map{_1=="A"? "AB": "A"}.join
}

# Kaneyklov (88b):
s='';(gets.to_i).times{puts _1==0?s='A' :s=s.gsub('A','C').gsub('B','A').gsub('C','AB')}

# Even shorter? (<60b):
