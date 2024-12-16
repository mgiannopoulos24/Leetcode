class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Initialize variables for the largest and smallest numbers
        max1 = max2 = float('-inf')
        min1 = min2 = float('inf')
        
        for num in nums:
            # Update the largest two numbers
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
            
            # Update the smallest two numbers
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        
        # Calculate the product difference
        return (max1 * max2) - (min1 * min2)
