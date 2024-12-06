from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        max_xor = (1 << maximumBit) - 1  # 2^maximumBit - 1
        xor_sum = 0
        
        # Calculate initial xor_sum of all elements in nums
        for num in nums:
            xor_sum ^= num
        
        result = []
        
        # Process queries in reverse order
        for i in range(n - 1, -1, -1):
            # Append the answer for the current state of xor_sum
            result.append(xor_sum ^ max_xor)
            # Remove the last element from xor_sum for the next query
            xor_sum ^= nums[i]
        
        return result
