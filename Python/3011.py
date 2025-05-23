from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Helper function to count set bits
        def count_bits(x):
            return bin(x).count('1')
        
        n = len(nums)
        i = 0
        prev_max = float('-inf')

        while i < n:
            current_bit_count = count_bits(nums[i])
            curr_min = nums[i]
            curr_max = nums[i]
            j = i + 1
            # Extend the segment as long as the bit count matches
            while j < n and count_bits(nums[j]) == current_bit_count:
                curr_min = min(curr_min, nums[j])
                curr_max = max(curr_max, nums[j])
                j += 1
            # Check if current segment min is >= previous segment max
            if curr_min < prev_max:
                return False
            prev_max = curr_max
            i = j  # Move to next segment

        return True