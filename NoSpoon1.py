# A straightforward way to solve this in O(n) where n is the number of nodes.

width = int(input())  # the number of cells on the X axis.
height = int(input())  # the number of cells on the Y axis

# An array to hold the coordinates string for each node that exists, 
# to be built up as we go along, and printed out at the end:
big_array = []
main_index = 0  # The node's index in the big_array.

# All existing nodes' main indices + coordinates, grouped by their row;
# easy peasy (i.e. O(1)) to find the next node to the right.
rows_array = [[] for row in range(height)]

# All existing nodes' main indices + coordinates, grouped by their column;
# easy peasy (i.e. O(1)) to find the next node below.
columns_array = [[] for column in range(width)]

# Go through all the nodes the first time:
for y in range(height):
    line = input()  # Characters representing if there is a node (0) or not (.)
    for x, char in enumerate(line):
        if char == "0":
            coordinates = "{} {} ".format(x, y)
            big_array.append(coordinates)
            rows_array[y].append("{}={}".format(main_index, coordinates))
            columns_array[x].append("{}={}".format(main_index, coordinates))
            main_index += 1

# Go through the rows_array to add all the nodes to the right of each node (or -1 -1)
for row in rows_array:
    for i, node in enumerate(row):
        node_index, coordinates = node.split("=")
        node_index = int(node_index)
        if i < len(row) - 1:
            next_node = row[i + 1]
            next_node_i, next_coord = next_node.split("=")
            big_array[node_index] += next_coord
        else:
            big_array[node_index] += "-1 -1 "

# Go through the columns_array for the nodes below each node.
for column in columns_array:
    for i, node in enumerate(column):
        node_index, coordinates = node.split("=")
        node_index = int(node_index)
        if i < len(column) - 1:
            next_node = column[i + 1]
            next_node_i, next_coord = next_node.split("=")
            big_array[node_index] += next_coord
        else:
            big_array[node_index] += "-1 -1"

# Go through the big_array in order of its main indices and print each node's coordinate set one at a time:
for coord in big_array:
    print(coord)