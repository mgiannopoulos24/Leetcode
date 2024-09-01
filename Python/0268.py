from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Calculate the expected sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2
        # Calculate the actual sum of the numbers in the array
        actual_sum = sum(nums)
        # The missing number is the difference between the expected and actual sums
        return expected_sum - actual_sum
