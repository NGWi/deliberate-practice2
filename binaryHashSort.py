r"""
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
     /   \       /  
  00      01    10     
 /   \    / \     \     
-3   -2  -1  0     2     
"""

import math


def countingHash(arr):
    '''
    Create a hash map to store the count of each integer, and retrieve the min and the max.
    '''
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


def treeSet(arr: list, offset: int, layers: int) -> set: # Could also try iterating through the counted_map keys. Less entries but not array.
    """
    Build a tree on top of the hashed values in another hash (python set). The tree has layers = int(log 2 ( max - min)).
    """
    tree = set()
    for num in arr:
        binary = bin(num - offset)[2:]
        key = binary.zfill(layers + 1)
        for i in range(layers):
            key = key[:-1]
            tree.add(key)
    return tree


def expandTree(tree: set, layers: int) -> list:
    """
    We expand the layers one at a time (breadth-first). The nodes are inherently ordered by 0, 1.
    """
    parent_layer = [""]
    for i in range(layers):
        child_layer = []
        for parent in parent_layer:
            for child in (parent + "0", parent + "1"):
                if child in tree:
                    child_layer.append(child)
        parent_layer = child_layer  # Can skip last one and do while True with if i < layer. See below

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

    return sorted_arr


def binaryHashSort(arr):
    counted_map, min_val, max_val = countingHash(arr)
    spread = max_val - min_val
    layers = int(math.log2(spread))
    tree = treeSet(arr, min_val, layers)
    last_parent_layer = expandTree(tree, layers)
    return sortedArray(last_parent_layer, counted_map, min_val)


# example_a = [0, 1, 2, 3, 4, 5, 6, 7]
# example_b = [-2, 0, -3, -1, 2]
# # print(treeSet(example_a, 0, int(math.log2(7 - 0))))
# print(binaryHashSort(example_a))
# print("-" * 10)
# print(binaryHashSort(example_b))
# print("=" * 20)


def expandTree2(tree: set, layers: int) -> list:
    """
    We expand the layers with a BFS. The nodes are inherently ordered by 0, 1.
    """
    parent_layer = [""]
    layer = 1
    while True:
        child_layer = []
        for parent in parent_layer:
            for child in (parent + "0", parent + "1"):
                if child in tree:
                    child_layer.append(child)
        if layer < layers:
            parent_layer = child_layer
        else:
            return child_layer
        layer += 1
def binaryHashSort2(arr):
    counted_map, min_val, max_val = countingHash(arr)
    spread = max_val - min_val
    layers = int(math.log2(spread))
    tree = treeSet(arr, min_val, layers)
    last_parent_layer = expandTree2(tree, layers)
    return sortedArray(last_parent_layer, counted_map, min_val)


# print(binaryHashSort2(example_a))
# print("-" * 10)
# print(binaryHashSort2(example_b))

import random
import time
def compare_binary_hash_sorts():
    n = 10000
    loops = 1000
    times = [0, 0]
    for int_r in [100, 1000, 10000, 100000, 1000000, 10000000]:
      print(f"int_r = {int_r}")
      for _ in range(loops):
          arr = [random.randint(-int_r, int_r - 1) for _ in range(n)]
          
          methods = [binaryHashSort, binaryHashSort2]
          for i, method in enumerate(methods):
              start_time = time.time()
              method(arr)
              end_time = time.time()
              times[i] += end_time - start_time
            
      print(f"binary hash sort took {times[0]/loops} seconds")
      print(f"binary hash sort 2 took {times[1]/loops} seconds")

# compare_binary_hash_sorts()

'''
int_r = 100
binary hash sort took 0.006196232557296753 seconds
binary hash sort 2 took 0.006134189367294311 seconds !
int_r = 1000
binary hash sort took 0.014297526359558105 seconds
binary hash sort 2 took 0.01420565152168274 seconds !
int_r = 10000
binary hash sort took 0.03198292970657349 seconds
binary hash sort 2 took 0.031715054750442506 seconds !
int_r = 100000
binary hash sort took 0.05809140777587891 seconds
binary hash sort 2 took 0.05797604608535767 seconds !
int_r = 1000000
binary hash sort took 0.09291549491882324 seconds !
binary hash sort 2 took 0.09309216022491455 seconds
int_r = 10000000
binary hash sort took 0.13956562399864197 seconds !
binary hash sort 2 took 0.13973849058151244 seconds
'''
import timeit
import matplotlib.pyplot as plt

ns = [100, 200, 300, 1000, 2000, 3000, 10000, 20000, 30000, 100000, 200000, 300000, 1000000, 2000000, 3000000]
times = []
loops = 10
for n in ns:
    print("Calculating for n = ", n)
    time = 0
    for _ in range(loops):
      arr = [random.randint(-n, n - 1) for _ in range(n)]
      time += timeit.timeit(lambda: binaryHashSort(arr), number=1)
    
    print("time = ", time/loops)
    times.append(time/n)

print("Plotting results")
plt.plot(ns, times)
plt.xlabel('n')
plt.ylabel('time')
plt.title('binaryHashSort performance')
plt.show()
