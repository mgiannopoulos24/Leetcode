class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Initialize variables
        seen = set()  # Set to keep track of unique elements
        current_sum = 0  # Sum of the current subarray
        max_sum = 0  # Maximum sum of a subarray
        start = 0  # Starting pointer of the sliding window
        
        # Iterate through the array with the 'end' pointer
        for end in range(len(nums)):
            # If the element is already in the set, slide the 'start' pointer to the right
            while nums[end] in seen:
                seen.remove(nums[start])
                current_sum -= nums[start]
                start += 1
            
            # Add the current element to the set and update the current sum
            seen.add(nums[end])
            current_sum += nums[end]
            
            # Update the maximum sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum
