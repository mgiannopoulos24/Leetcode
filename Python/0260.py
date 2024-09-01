from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all numbers to get the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Step 2: Find a bit that is set in xor_all (this bit is different between the two unique numbers)
        diff_bit = xor_all & -xor_all
        
        # Step 3: Partition the numbers into two groups and find the unique number in each group
        unique1, unique2 = 0, 0
        for num in nums:
            if num & diff_bit:
                unique1 ^= num
            else:
                unique2 ^= num
        
        return [unique1, unique2]
