import heapq

class DinnerPlates:
    def __init__(self, capacity: int):
        """
        Initialize the DinnerPlates object with the maximum capacity of each stack.
        """
        self.capacity = capacity
        self.stacks = []  # List of stacks
        self.min_heap = []  # Min heap to track the leftmost stack with available space
        self.max_heap = []  # Max heap (using negative indices) to track the rightmost non-empty stack
        self.right = -1  # Track the current rightmost non-empty stack

    def push(self, val: int) -> None:
        """
        Pushes the given integer val into the leftmost stack with a size less than capacity.
        """
        # Clean up the min_heap to find the first stack that has space
        while self.min_heap:
            index = heapq.heappop(self.min_heap)
            if index < len(self.stacks) and len(self.stacks[index]) < self.capacity:
                heapq.heappush(self.min_heap, index)
                break
        else:
            index = len(self.stacks)
            self.stacks.append([])

        # Push the value to the identified stack
        heap_index = self.min_heap[0] if self.min_heap else index
        if self.min_heap:
            heap_index = heapq.heappop(self.min_heap)
        else:
            heap_index = index

        # If the stack index is beyond current stacks, extend the stacks
        while heap_index >= len(self.stacks):
            self.stacks.append([])

        self.stacks[heap_index].append(val)

        # If the stack still has space, push it back to min_heap
        if len(self.stacks[heap_index]) < self.capacity:
            heapq.heappush(self.min_heap, heap_index)

        # Update the max_heap with the current stack index
        heapq.heappush(self.max_heap, -heap_index)
        # Update the right pointer
        self.right = max(self.right, heap_index)

    def pop(self) -> int:
        """
        Returns the value at the top of the rightmost non-empty stack and removes it from that stack,
        and returns -1 if all the stacks are empty.
        """
        while self.max_heap:
            index = -heapq.heappop(self.max_heap)
            if index < len(self.stacks) and self.stacks[index]:
                val = self.stacks[index].pop()
                # After popping, if there's space, add back to min_heap
                if len(self.stacks[index]) < self.capacity:
                    heapq.heappush(self.min_heap, index)
                # If the stack still has plates, push it back to max_heap
                if self.stacks[index]:
                    heapq.heappush(self.max_heap, -index)
                else:
                    # Update the right pointer
                    if index == self.right:
                        self.right -= 1
                        while self.right >=0 and (self.right >= len(self.stacks) or not self.stacks[self.right]):
                            self.right -=1
                return val
        return -1

    def popAtStack(self, index: int) -> int:
        """
        Returns the value at the top of the stack with the given index and removes it from that stack
        or returns -1 if the stack with that given index is empty.
        """
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            val = self.stacks[index].pop()
            # After popping, if there's space, add to min_heap
            if len(self.stacks[index]) < self.capacity:
                heapq.heappush(self.min_heap, index)
            # If the stack becomes empty, and it's the current rightmost, update right
            if not self.stacks[index]:
                if index == self.right:
                    self.right -=1
                    while self.right >=0 and (self.right >= len(self.stacks) or not self.stacks[self.right]):
                        self.right -=1
            return val
        return -1

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)