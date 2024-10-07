from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Get the length of the array
        n = len(nums)
        # Initialize the result array with the same length
        result = [0] * n
        
        # Pointers for the left and right ends of the array
        left, right = 0, n - 1
        # Position to fill in the result array (start from the end)
        position = n - 1
        
        # Process the array until all positions are filled
        while left <= right:
            # Square the values at the pointers
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            # Compare squares and place the larger one at the current position
            if left_square > right_square:
                result[position] = left_square
                left += 1
            else:
                result[position] = right_square
                right -= 1
            
            # Move the position pointer to the left
            position -= 1
        
        return result
