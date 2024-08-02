# Write a function that takes in a string of code with parentheses, square brackets, and curly brackets, and checks if the code is balanced with correct bracket syntax.

# A relatively short and straightforward solution in O(n):

example_a = "(x+3)[y{3}(z]"
example_b = "([[{}]])"
example_c = ""
example_d = "(][)"
new_example = "([{<>)}]"

def balance(string)
  puts string
  brackets_ref = {"]"=>"[",")"=>'(',"}"=>"{", ">"=>"<"}
  opening_ref = {"["=>true,"("=>true,"{"=>true,"<"=>true}
  opening_found = []
  string.each_char {|char|
    if brackets_ref.include?(char)
      if brackets_ref[char] == opening_found[-1]
        opening_found.pop
      else
        return "NOT BALANCED"
      end
    elsif opening_ref.include?(char)
      opening_found << char
    end
  }
  return "BALANCED"
end

puts balance(example_a)
puts "-" * 20
puts balance(example_b) 
puts "-" * 20
puts balance(example_c)
puts "-" * 20
puts balance(example_d)
puts "-" * 20
puts balance(new_example) 