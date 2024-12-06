from itertools import permutations

class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        max_value = 0
        
        # Generate all permutations of nums
        for perm in permutations(nums):
            # Convert the numbers in the permutation to binary strings and concatenate them
            concatenated_binary = ''.join(bin(num)[2:] for num in perm)
            
            # Convert the concatenated binary string to a decimal number
            decimal_value = int(concatenated_binary, 2)
            
            # Update the maximum value
            max_value = max(max_value, decimal_value)
        
        return max_value
