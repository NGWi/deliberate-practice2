class MinHeap:
    def __init__(self):
        # Initialize with empty array
        self.heap = []
    
    def parent_idx(self, idx):
        """Get index of parent node"""
        return (idx - 1) // 2
    
    def left_child_idx(self, idx):
        """Get index of left child"""
        return 2 * idx + 1
    
    def right_child_idx(self, idx):
        """Get index of right child"""
        return 2 * idx + 2
    
    def swap(self, i, j):
        """Swap elements at indices i and j"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def push(self, value):
        """Add new value to heap"""
        # 1. Add value to end of array
        self.heap.append(value)
        # 2. Bubble up until heap property is restored
        self._bubble_up(len(self.heap) - 1)
    
    def _bubble_up(self, idx):
        """Move element up until parent is smaller"""
        # While we're not at root and parent is larger
        while idx > 0 and self.heap[self.parent_idx(idx)] > self.heap[idx]:
            parent = self.parent_idx(idx)
            # Swap with parent
            self.swap(idx, parent)
            # Move up to parent's position
            idx = parent
    
    def pop(self):
        """Remove and return smallest element"""
        if not self.heap:
            return None
            
        # 1. Save minimum value (root)
        min_val = self.heap[0]
        
        # 2. Move last element to root
        last_val = self.heap.pop()
        if self.heap:  # If heap isn't empty now
            self.heap[0] = last_val
            # 3. Bubble down until heap property is restored
            self._bubble_down(0)
            
        return min_val
    
    def _bubble_down(self, idx):
        """Move element down until children are larger"""
        min_idx = idx
        size = len(self.heap)
        
        while True:
            # Check both children to find smallest
            left = self.left_child_idx(idx)
            right = self.right_child_idx(idx)
            
            # Update min_idx if left child is smaller
            if left < size and self.heap[left] < self.heap[min_idx]:
                min_idx = left
                
            # Update min_idx if right child is smaller
            if right < size and self.heap[right] < self.heap[min_idx]:
                min_idx = right
            
            # If neither child is smaller, we're done
            if min_idx == idx:
                break
                
            # Swap with smaller child and continue down
            self.swap(idx, min_idx)
            idx = min_idx
    
    def peek(self):
        """Return smallest element without removing it"""
        return self.heap[0] if self.heap else None
    
    def size(self):
        """Return number of elements in heap"""
        return len(self.heap)


# Example usage:
if __name__ == "__main__":
    # Create heap
    heap = MinHeap()
    
    # Add some numbers
    numbers = [5, 3, 8, 1, 2, 7, 4]
    print("Adding numbers:", numbers)
    for num in numbers:
        heap.push(num)
        print(f"Added {num}. Heap is now: {heap.heap}")
    
    # Pop all numbers (will come out in sorted order)
    print("\nRemoving numbers:")
    while heap.size() > 0:
        num = heap.pop()
        print(f"Removed {num}. Heap is now: {heap.heap}")
