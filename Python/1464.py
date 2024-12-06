class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize two maximums
        first_max = second_max = float('-inf')
        
        # Loop through the array to find the two largest numbers
        for num in nums:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num
        
        # Compute the maximum product
        return (first_max - 1) * (second_max - 1)
