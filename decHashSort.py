r"""
The idea of this sort is a level beyond wiseCountingSort. It's point is to eliminate the independent + r factor where r is the size of the range.
See binaryHashSort for a binary implementation. This one will use the 'regular' decimal base to avoid having to convert the list numbers one round trip between binary and decimal. However, theoretically 2 or 3 are better bases ~1.5:1 because the time complexity is ~ O(b * n * log b n).
I do the first pass through the array to make the wiseCounting Hash (python dict).
Now that I have the min and max values, I make another pass to build a tree on top of the hashed values in another hash (python set). The tree has layers = int(log 2 ( max - min)). 
Each node is a key. It will equal the lowest of its two children with the last digit removed, and, correspondingly will have a length of 1 more than its parent node. If neither of its children exist then it wouldn't either exist.
The we expand the layers one layer at a time breadth-first. The nodes are inherently ordered by 0, 1. When we have expanded it by `layers` then we append the occurences of the end numbers to the sorted array as in WiseCountingSort.

Example input = [15, 3, 14, 7, 3, 9, 3, 7, 8, 0, 12, 11, 16, 8, 15, 10, 15, 9, 14, 5]
Example hashes =      {15: 3, 3: 3, 14: 2, 7: 2, 9: 2, 8: 2, 0: 1, 12: 1, 11: 1, 16: 1, 10: 1, 5: 1}
Sorted visualization: {0: 1, 3: 3, 5: 1, 7: 2, 8: 2, 9: 2, 10: 1, 11: 1, 12: 1, 14: 2, 15: 3, 16: 1}
min = 0, max = 16, layers = 1.
Example tree =  {'0', '1'} 

Tree-like visualization:
            /                         /
          0                          1
   /     /  |  \ \ \      /  /  /    |  \  \
  0     3   5   7 8 9   10 11 12    14   15 16
  1     3   1   2 2 2    1  1  1     2    3  1
 
 Example B = [3, -12, 2, 9, -6, 14, -7, -4, -19, -5, -12, 2, -8, 15, 6, 18, 2, 11, -2, -2]
 
 Tree-like visualization:
            /                            /                        /                  /
          0                             1                        2                  3
    /           \               /  /  /  | \    \          /  /  |        /     /   |      \   
  -19           -12            -8 -7 -6 -5 -4   -2         2 3   6      11     14   15     18  
"""

import math


def countingHash(arr: list) -> tuple:
    """
    Create a hash map to store the count of each integer, and retrieve the min and the max.
    """
    counted_map = {arr[0]: 1}
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

    return counted_map, min_val, max_val


def treeSet(
    arr: list, offset: int, layers: int
) -> (
    set
):  # Could also try iterating through the counted_map keys. Less entries but not array.
    """
    Build a tree on top of the hashed values in another hash (python set). The tree has layers = int(log 10 ( max - min)).
    """
    tree = set()
    for num in arr:
        offset_num = num - offset
        key = str(offset_num).zfill(layers + 1)
        for _ in range(layers):
            key = key[
                :-1
            ]  # Have to think of a way to start with a layers length string and just not cut off before the first.
            tree.add(key)

    return tree


def expandTree(tree: set, layers: int) -> list:
    """
    We expand the layers one at a time (breadth-first). The nodes are inherently ordered by 0...9.
    """
    parent_layer = [""]
    for i in range(layers):
        child_layer = []
        for parent in parent_layer:
            for i in range(10):
                child = parent + str(i)
                if child in tree:
                    child_layer.append(child)
        parent_layer = child_layer  # Can skip last one and do while True with if i < layer. See below

    return parent_layer


def sortedArray(last_parent_layer: list, counted_map: dict, offset: int) -> list:
    """
    Make one pass through the parent_layer to construct the sorted array.
    """
    sorted_arr = []
    for parent in last_parent_layer:
        for i in range(10):
            child = parent + str(i)
            num = int(child) + offset
            if num in counted_map:
                sorted_arr.extend([num] * counted_map[num])

    return sorted_arr


def shortArr(counted_map: dict, min_val: int, max_val: int) -> list:
    """
    Simple build for arrays with under a 10 number spread between min and max, from original Wise Counting Sort.
    """
    short_arr = []
    for i in range(min_val, max_val + 1):
        if i in counted_map:
            short_arr.extend([i] * counted_map[i])
    return short_arr


def decHashSort(arr: list) -> list:
    counted_map, min_val, max_val = countingHash(arr)
    spread = max_val - min_val
    if spread != 0:
        layers = int(math.log10(spread))
        tree = treeSet(arr, min_val, layers)
        last_parent_layer = expandTree(tree, layers)
        return sortedArray(last_parent_layer, counted_map, min_val)
    else:
        return shortArr(counted_map, min_val, max_val)


# example_a = [15, 3, 14, 7, 3, 9, 3, 7, 8, 0, 12, 11, 16, 8, 15, 10, 15, 9, 14, 5]
# example_b = [3, -12, 2, 9, -6, 14, -7, -4, -19, -5, -12, 2, -8, 15, 6, 18, 2, 11, -2, -2]
# print(decHashSort(example_a))
# print("-" * 10)
# print(decHashSort(example_b))
# print("=" * 20)


def compare_hash_sorts():
    import timeit
    import random
    from binaryHashSort import binaryHashSort

    for int_r in [100, 1000, 10000, 100000, 1000000, 10000000]:
        print("int_r = ", int_r)
        arr = [random.randint(-int_r, int_r - 1) for _ in range(int_r)]
        print(
            "dec hash sort took ",
            timeit.timeit(lambda: decHashSort(arr), number=10),
            " seconds",
        )
        print(
            "binary hash sort took ",
            timeit.timeit(lambda: binaryHashSort(arr), number=10),
            " seconds",
        )
        assert decHashSort(arr) == binaryHashSort(arr)
        print("-" * 10)


# compare_hash_sorts()
