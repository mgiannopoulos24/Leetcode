from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Find the minimum value in the array
        min_val = min(nums)
        
        # Calculate the total number of moves needed
        moves = 0
        for num in nums:
            # Increment moves by the difference between the current number and the minimum value
            moves += num - min_val
        
        return moves
