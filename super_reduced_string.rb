#!/bin/ruby

require 'json'
require 'stringio'

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
example_a = "aaabccddd"
example_b = ""
example_c = "abcddcba"
def match(s, index)

end
    
def superReducedString(s)
    # Write your code here
    length = s.length
    index = length - 1
    while index >= 1
      letter = s[index]
      next_l = s[index - 1]
      pp letter, next_l
      if letter == next_l
          pp "A match."
          s.slice!(index)
          s.slice!(index - 1)
          pp s + " after reduction."
      else
          pp "Moving on"
      end 
      pp "Next letter."
      index -= 1
      pp index
    end
    if s == ""
        "Empty String"
    else
        s
    end
end

# fptr = File.open(ENV['OUTPUT_PATH'], 'w')

# s = gets.chomp

pp superReducedString example_a
puts "-" * 20
pp superReducedString example_b
puts "-" * 20
pp superReducedString example_c

# fptr.write result
# fptr.write "\n"

# fptr.close()