class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Step 1: Sort the array and keep track of the original index
        sorted_nums = sorted(nums)
        
        # Step 2: Create a dictionary that maps each number to the count of numbers smaller than it
        count_smaller = {}
        
        for i, num in enumerate(sorted_nums):
            # If the number is not yet in the dictionary, set its value to the index
            if num not in count_smaller:
                count_smaller[num] = i
        
        # Step 3: Build the result array using the original nums array
        result = [count_smaller[num] for num in nums]
        
        return result
