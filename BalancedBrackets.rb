# Write a function that takes in a string of code with parentheses, square brackets, and curly brackets, and checks if the code is balanced with correct bracket syntax.

example_a = "(x+3)[y{3}(z]"
example_b = "([[{}]])"
example_c = ""
example_d = "(][)"
new_example = "([{<>)}]"

def balance(string)
  puts string
  closing = {"]"=>0,")"=>1,"}"=>2, ">"=>3}
  opening = ["[","(","{","<"]
  index = 0
  length = string.length
  while index < length
    looking_for = nil
    found_i = nil
    while index < length
      char = string[index]
      if closing[char]
        found_i = index
        opening_i = closing[char]
        looking_for = opening[opening_i]
        wrong_brackets = opening.dup
        wrong_brackets.delete_at(opening_i)
        break
      else
        # puts "Not yet"
      end
      index += 1
    end
    
    if looking_for
      puts "Closing Brackets found at index: " + index.to_s
      puts looking_for
      puts "Wrong Brackets: " + wrong_brackets.to_s
    else
      puts "No Brackets"
      puts "BALANCED"
      return
    end

    index -= 1

    found_match = false
    while index >= 0
      char = string[index]
      if char == looking_for
        puts "Found"
        found_match = true
        string.slice!(found_i)
        string.slice!(index)
        index = found_i - 1
        break
      elsif wrong_brackets.include?(char)
        puts "NOT BALANCED"
        return
      end
      index -= 1
    end
    if found_match == false
      puts "NOT BALANCED"
      return
    end
    puts "String left: " + string
  end
  puts "BALANCED"
end

balance(example_a)
puts "-" * 20
balance(example_b) 
puts "-" * 20
balance(example_c)
puts "-" * 20
balance(example_d)
puts "-" * 20
balance(new_example) 