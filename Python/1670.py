class FrontMiddleBackQueue:

    def __init__(self):
        self.left = []  # Left half of the queue
        self.right = []  # Right half of the queue

    def rebalance(self):
        # Ensure that the left half has the same number of elements or at most one more than the right half.
        if len(self.left) > len(self.right) + 1:
            self.right.insert(0, self.left.pop())  # Move one element from left to right
        elif len(self.right) > len(self.left):
            self.left.append(self.right.pop(0))  # Move one element from right to left

    def pushFront(self, val: int) -> None:
        self.left.insert(0, val)  # Insert into the left half (front)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) > len(self.right):
            self.right.insert(0, self.left.pop())  # Shift one element from left to right before inserting in the middle
        self.left.append(val)  # Insert into the middle of the left half
        self.rebalance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)  # Insert into the right half (back)
        self.rebalance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1  # Queue is empty
        if self.left:
            val = self.left.pop(0)  # Pop from the front of the left half
        else:
            val = self.right.pop(0)  # Pop from the front of the right half if left is empty
        self.rebalance()
        return val

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1  # Queue is empty
        if len(self.left) == len(self.right):
            val = self.left.pop()  # Pop from the back of the left half if balanced
        else:
            val = self.left.pop()  # Otherwise, pop from the back of the left half (since it's larger)
        self.rebalance()
        return val

    def popBack(self) -> int:
        if not self.left and not self.right:
            return -1  # Queue is empty
        if self.right:
            val = self.right.pop()  # Pop from the back of the right half
        else:
            val = self.left.pop()  # If the right is empty, pop from the back of the left half
        self.rebalance()
        return val
