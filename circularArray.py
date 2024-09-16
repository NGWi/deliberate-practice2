def is_positive(num):
  if num < 0:
    return False
  else:
    return True

def move_pointer(index, move, length):
  print("Moving pointer", index, "+", move)
  target = index + move
  while target >= length:
    target -= length
  while target < 0:
    target += length
  print (target)
  return target
  
  
def circular_array_loop(nums):
  index = 0
  length = len(nums)
  while index < length:
    slow = index
    med = 0
    fast = move_pointer(index, nums[index], length)
    direction = is_positive(nums[slow])
    print(fast, slow)
    index += 1
    if slow == fast:
      continue
    while True:
        next = move_pointer(slow, nums[slow], length) 
        if next == slow or is_positive(nums[slow]) != direction:
          break
        else:
          slow = next
        
        next =  move_pointer(fast, nums[fast], length)
        if next == fast or is_positive(nums[med]) != direction:
          break
        else: 
          med = next
        
        next = move_pointer(med, nums[med], length)
        if next == med or is_positive(nums[fast]) != direction:
          break
        else: 
          fast = next
        
        if slow == fast:
          return True

  return False

print(circular_array_loop([1,3,-2,-4,1]))
print("*" * 10)
print(circular_array_loop([2,1,-1,-2]))
print("*" * 10)
print(circular_array_loop([5,4,-2,-1,3]))
print("*" * 10)
print(circular_array_loop([1,2,-3,3,4,7,1]))
print("*" * 10)
print(circular_array_loop([3,3,1,-1,2]))
print("*" * 10)
print(circular_array_loop([1,1,1,1,1]))
print("*" * 10)
print(circular_array_loop([1, 2, 3, 4, 5, 6]))
print("*" * 10)
print(circular_array_loop([0, 0, 0, 0, 0, 0]))

input = (
        [-2, -3, -9],
        [-5, -4, -3, -2, -1],
        [-1, -2, -3, -4, -5],
        [2, 1, -1, -2],
        [-1, -2, -3, -4, -5, 6],
        [1, 2, -3, 3, 4, 7, 1],
        [2, 2, 2, 7, 2, -1, 2, -1, -1]
        )
num = 1

for i in input:
    print(f"{num}.\tCircular array = {i}")
    print(f"\n\tFound loop = {circular_array_loop(i)}")
    print("-"*100, "\n")
    num += 1