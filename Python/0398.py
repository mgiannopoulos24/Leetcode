import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.index_map = {}
        for index, num in enumerate(nums):
            if num not in self.index_map:
                self.index_map[num] = []
            self.index_map[num].append(index)

    def pick(self, target: int) -> int:
        return random.choice(self.index_map[target])

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)