class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix_sum_set = {0}  # Initialize with 0 to handle subarrays starting from index 0
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            # If current_sum - target exists in the set, it means we found a subarray with sum target
            if current_sum - target in prefix_sum_set:
                count += 1
                # Reset the set and sum to start searching for a new non-overlapping subarray
                prefix_sum_set = {0}
                current_sum = 0
            else:
                # Add the current sum to the set
                prefix_sum_set.add(current_sum)
        
        return count
