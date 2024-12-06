class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # If the array has less than or equal to 4 elements, we can change all elements to the same value in at most 3 moves.
        if len(nums) <= 4:
            return 0
        
        # Sort the array
        nums.sort()
        
        # After sorting, we have four possibilities to minimize the difference:
        # 1. Change the 3 largest elements.
        # 2. Change the 2 largest elements and the smallest element.
        # 3. Change the largest element and the 2 smallest elements.
        # 4. Change the 3 smallest elements.
        # We return the minimum difference after each of these scenarios.
        return min(nums[-1] - nums[3],  # Remove the 3 smallest elements
                   nums[-2] - nums[2],  # Remove the 2 smallest and 1 largest element
                   nums[-3] - nums[1],  # Remove the 1 smallest and 2 largest elements
                   nums[-4] - nums[0])  # Remove the 3 largest elements
