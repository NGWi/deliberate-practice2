# https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-1
# A straightforward way to solve this in O(n) where n is the number of nodes.

STDOUT.sync = true # CodinGame runtime optimization.

width = gets.to_i   # the number of cells on the X axis.

height = gets.to_i  # the number of cells on the Y axis

# An array to hold the coordinates string for each node that exists,
# to be built up as we go along, and printed out at the end:
# Example members: "0 0 1 0 0 1", "1 0 -1 -1 -1 -1"
big_array = []
main_index = 0          # The node's index in the big_array.

# All existing nodes' main indices + coordinates, grouped by their row;
# easy peasy (i.e. O(1)) to find the next node to the right.
# Example members: [0=0 0, 1=1 0], [2=0 1]
rows_array = []
height.times {
  rows_array << []      # Indexed placeholders for the rows.
}

# All existing nodes' main indices + coordinates, grouped by their column;
# easy peasy (i.e. O(1)) to find the next node below.
# Example members: [0=0 0, 2=0 1], [1=1 0]
columns_array = []
width.times {
  columns_array << []   # Indexed placeholders for the columns.
}

# Go through all the nodes the first time:
y = 0
height.times {
  x = 0
  line = gets.chomp     # Characters representing if there is a node (0) or not (.)
  line.each_char { |char|
    if char == "0"
      coordinates = "#{x} #{y} "
      big_array[main_index] = coordinates
      rows_array[y] << main_index.to_s + "=" + coordinates
      columns_array[x] << main_index.to_s + "=" + coordinates
      main_index += 1
    end
    x += 1
  }
  y += 1
}

# Go through the rows_array to add all the nodes to the right of each node (or -1 -1)
rows_array.each { |row|
  length = row.length
  index = 0
  while index < length
    node = row[index]
    next_node = row[index + 1]
    node_index = node.split("=")[0].to_i
    if next_node
      next_coord = next_node.split("=")[1]
      big_array[node_index] += next_coord
    else
      big_array[node_index] += "-1 -1 "
    end
    index += 1
  end
}

# Go through the columns_array for the nodes below each node.
columns_array.each { |column|
  length = column.length
  index = 0
  while index < length
    node = column[index]
    next_node = column[index + 1]
    node_index = node.split("=")[0].to_i
    if next_node
      next_coord = next_node.split("=")[1]
      big_array[node_index] += next_coord
    else
      big_array[node_index] += "-1 -1"
    end
    index += 1
  end
}

# Go through the big_array in order of its main indices and print each node's coordinate set one at a time:
index_to_print = 0
total = big_array.length
while index_to_print
  puts big_array[index_to_print]
  index_to_print += 1
end
