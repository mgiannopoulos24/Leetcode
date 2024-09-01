from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        # Initialize the prefix sum array
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Calculate the sum of the range [left, right] using the prefix sum array
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
