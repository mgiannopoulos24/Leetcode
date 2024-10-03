class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            max_ending_here = max_so_far = arr[0]
            for x in arr[1:]:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        
        def min_kadane(arr):
            min_ending_here = min_so_far = arr[0]
            for x in arr[1:]:
                min_ending_here = min(x, min_ending_here + x)
                min_so_far = min(min_so_far, min_ending_here)
            return min_so_far
        
        total_sum = sum(nums)
        max_sum = kadane(nums)
        min_sum = min_kadane(nums)
        
        # If all numbers are negative, max_sum will be the best answer
        if total_sum == min_sum:
            return max_sum
        
        return max(max_sum, total_sum - min_sum)
