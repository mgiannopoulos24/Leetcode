from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        
        for num in nums:
            # Update twos with bits that are already in ones and are also in current number
            twos |= ones & num
            # Update ones with new bits from current number
            ones ^= num
            # Determine the mask for bits that appear three times
            threes = ones & twos
            # Remove the bits that appeared three times from ones and twos
            ones &= ~threes
            twos &= ~threes
        
        return ones
