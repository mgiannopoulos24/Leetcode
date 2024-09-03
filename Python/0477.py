from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total_distance = 0
        
        # Iterate through each bit position
        for bit in range(32):  # 32-bit integers
            count_one = 0
            for num in nums:
                # Count how many numbers have a `1` at the current bit position
                if num & (1 << bit):
                    count_one += 1
            
            # Number of numbers that have a `0` at the current bit position
            count_zero = n - count_one
            
            # Each pair with different bits at this position contributes to the Hamming distance
            total_distance += count_one * count_zero
        
        return total_distance
