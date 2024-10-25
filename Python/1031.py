from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # Function to calculate the maximum sum of two non-overlapping subarrays
        def max_sum(L: int, M: int) -> int:
            n = len(nums)
            # Precompute prefix sums for fast range sum queries
            prefix_sum = [0] * (n + 1)
            for i in range(1, n + 1):
                prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
            
            # maxL stores the maximum sum of L-length subarray seen so far
            maxL = 0
            result = 0
            
            # Iterate through the array, ensuring L-length subarray comes before M-length
            for i in range(L + M, n + 1):
                maxL = max(maxL, prefix_sum[i - M] - prefix_sum[i - M - L])  # Maximum L-length subarray before current M-length
                result = max(result, maxL + prefix_sum[i] - prefix_sum[i - M])  # L + M combination
            
            return result
        
        # Case 1: FirstLen comes before SecondLen
        case1 = max_sum(firstLen, secondLen)
        # Case 2: SecondLen comes before FirstLen
        case2 = max_sum(secondLen, firstLen)
        
        return max(case1, case2)
