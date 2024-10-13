"""
The idea of this sort is a level beyond wiseCountingSort. It's point is to eliminate the independant + r factor where r is the size of the range.
I do the first pass through the array to make the wiseCounting Hash (python dict).
Now that I have the min and max values, I make another pass to build a tree on top of the hashed values in another hash (python set). The tree has layers = int(log 2 ( max - min)). 
Each node is a binary key it will equal the lowest of its two children with the last digit removed, and, correspondingly will have a length of 1 more than its parent node. If neither of its children exist then it wouldn't either exist.
The we expand the layers with a BFS. The nodes are inherently ordered by 0, 1. When we have expanded it by `layers` then we append the occurences of the end numbers to the sorted array as in WiseCountingSort.

Example input = [3,5,2,4,1,0,6,7]
Example hashes = {3: 1, 5: 1, 2: 1, 4: 1, 1: 1, 0: 1, 6: 1, 7: 1} . 
Sorted visualization: {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}
min = 0, max = 7, layers = 2.
Example tree =  { '01', '0', '10', '1', '00', '11'} 
Sorted visualization: { '00', '01', '10', '11',
                        '0', '1'}

Tree-like visualization:
      /        \
     0          1
   /   \       / \
  00   01    10   11
 / \   / \   / \  / \
 0  1  2  3  4  5 6  7
 
 Example B = [-2, 0, -3, -1, 2]
 
 Tree-like visualization:
      /        \
     0          1
       \       / \
       01    10   11
       / \   / \    \
      -3 -2 -1  0    2
"""

import math


def countingHash(arr):
    # Create a hash map to store the count of each integer
    counted_map = {arr[0]: 1}
    # Make one pass through the array to count the occurrences of each integer and retrieve the min and max
    min_val = max_val = arr[0]
    for num in arr[1:]:
        if num in counted_map:
            counted_map[num] += 1
        else:
            counted_map[num] = 1
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    print("Counted map: ", counted_map)
    return counted_map, min_val, max_val


def treeSet(arr: list, offset: int, layers: int) -> set:
    """
    Build a tree on top of the hashed values in another hash (python set). The tree has layers = int(log 2 ( max - min)).
    """
    tree = set()
    for num in arr:
        binary = bin(num - offset)[2:]
        print(binary)
        key = binary.zfill(layers + 1)
        for i in range(layers):
            key = key[:-1]
            tree.add(key)
    print("Tree: ", tree)
    return tree


def expandTree(tree: set, layers: int) -> list:
    """
    We expand the layers with a BFS. The nodes are inherently ordered by 0, 1.
    """
    parent_layer = [""]
    for i in range(layers):
        print("Layer ", i, "Parent layer: ", parent_layer)
        child_layer = []
        for parent in parent_layer:
            for child in (parent + "0", parent + "1"):
                if child in tree:
                    child_layer.append(child)
        parent_layer = child_layer  # Can skip last one and do while True with if i < layer. See below

    print("Parent layer: ", parent_layer)
    return parent_layer


def sortedArray(last_parent_layer, counted_map, offset):
    """
    Make one pass through the parent_layer to construct the sorted array.
    """
    sorted_arr = []
    for parent in last_parent_layer:
        for child in (parent + "0", parent + "1"):
            num = int(child, 2) + offset
            if num in counted_map:
                sorted_arr.extend([num] * counted_map[num])

    print("Sorted array: ", sorted_arr)
    return sorted_arr


def binaryHashSort(arr):
    counted_map, min_val, max_val = countingHash(arr)
    spread = max_val - min_val
    layers = int(math.log2(spread))
    tree = treeSet(arr, min_val, layers)
    last_parent_layer = expandTree(tree, layers)
    return sortedArray(last_parent_layer, counted_map, min_val)


example_a = [0, 1, 2, 3, 4, 5, 6, 7]
example_b = [-2, 0, -3, -1, 2]
# print(treeSet(example_a, 0, int(math.log2(7 - 0))))
print(binaryHashSort(example_a))
print("-" * 10)
print(binaryHashSort(example_b))
print("=" * 20)


def expandTree2(tree: set, layers: int) -> list:
    """
    We expand the layers with a BFS. The nodes are inherently ordered by 0, 1.
    """
    parent_layer = [""]
    layer = 1
    while True:
        print("Layer ", layer, "Parent layer: ", parent_layer)
        child_layer = []
        for parent in parent_layer:
            for child in (parent + "0", parent + "1"):
                if child in tree:
                    child_layer.append(child)
        if layer < layers:
            parent_layer = child_layer
        else:
            print("Final parent layer: ", child_layer)
            return child_layer
        layer += 1


def binaryHashSort2(arr):
    counted_map, min_val, max_val = countingHash(arr)
    spread = max_val - min_val
    layers = int(math.log2(spread))
    tree = treeSet(arr, min_val, layers)
    last_parent_layer = expandTree2(tree, layers)
    return sortedArray(last_parent_layer, counted_map, min_val)


print(binaryHashSort2(example_a))
print("-" * 10)
print(binaryHashSort2(example_b))
