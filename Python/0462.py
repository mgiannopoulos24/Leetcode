from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        
        # Find the median
        median = nums[len(nums) // 2]
        
        # Calculate the total number of moves required to make all elements equal to the median
        moves = sum(abs(num - median) for num in nums)
        
        return moves
