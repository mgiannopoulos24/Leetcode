from typing import List
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def maxSumNoLargerThanK(arr: List[int], k: int) -> int:
            # This function finds the maximum sum of subarrays with sum <= k
            prefix_sum = [0]  # Initialize with 0 for the prefix sum
            curr_sum = 0
            max_sum = float('-inf')
            
            for num in arr:
                curr_sum += num
                # Use binary search to find the smallest prefix sum >= curr_sum - k
                idx = bisect.bisect_left(prefix_sum, curr_sum - k)
                if idx < len(prefix_sum):
                    max_sum = max(max_sum, curr_sum - prefix_sum[idx])
                bisect.insort(prefix_sum, curr_sum)
            
            return max_sum
        
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        
        for left in range(n):
            # Initialize the row sums array
            row_sums = [0] * m
            for right in range(left, n):
                # Compute the row sums for the columns between `left` and `right`
                for i in range(m):
                    row_sums[i] += matrix[i][right]
                # Find the maximum sum of the 1D subarray with sum <= k
                max_sum = max(max_sum, maxSumNoLargerThanK(row_sums, k))
        
        return max_sum
