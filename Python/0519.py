import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.flipped = {}
        self.available = self.total

    def flip(self) -> [int]:
        # Pick a random index from available
        rand_index = random.randint(0, self.available - 1)
        # Get the position (if previously flipped, get mapped value)
        pos = self.flipped.get(rand_index, rand_index)
        # Decrease the available slots
        self.available -= 1
        # Map the selected index to the last available unflipped index
        self.flipped[rand_index] = self.flipped.get(self.available, self.available)
        # Return the 2D index
        return [pos // self.n, pos % self.n]

    def reset(self) -> None:
        # Reset everything
        self.flipped.clear()
        self.available = self.total


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()