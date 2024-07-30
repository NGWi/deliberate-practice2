# https://screen-ide.coderpad.io/23996223
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n =  1     # gets.to_i

inputs =  "-10 -10" # gets

def negative_check(number)
  if number < 0
    number -= 0.1
  end
  number
end

def closest_temp(n, inputs)
  if inputs
    puts "inputs: #{inputs}"
    inputs = inputs.split
    puts "inputs: #{inputs}"
  else
    puts "inputs falsy"
    return 0
  end

  closest = inputs[0].to_i
  puts "closest: #{closest}"
  closest = negative_check(closest)
  puts "closest: #{closest}"

  index = 1
  while index < n
    puts "index: #{index}"
    number = negative_check(inputs[index].to_i)
    if number.abs < closest.abs
      closest = number
    end
    index += 1
  end
  if closest < 0
    closest += 0.1
    closest = closest.to_i
  end
  return closest
end

# Write an answer using puts
puts closest_temp(n, inputs)