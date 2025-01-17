from itertools import combinations
from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        left, right = nums[:n], nums[n:]
        
        # Generate all possible subset sums for the left and right halves
        left_sums = [[] for _ in range(n + 1)]
        right_sums = [[] for _ in range(n + 1)]
        
        # Generate subsets for the left half
        for mask in range(0, 1 << n):
            count = bin(mask).count('1')  # Number of elements in the subset
            total = 0
            for i in range(n):
                if mask & (1 << i):
                    total += left[i]
            left_sums[count].append(total)
        
        # Generate subsets for the right half
        for mask in range(0, 1 << n):
            count = bin(mask).count('1')  # Number of elements in the subset
            total = 0
            for i in range(n):
                if mask & (1 << i):
                    total += right[i]
            right_sums[count].append(total)
        
        # Sort the right_sums for binary search
        for i in range(n + 1):
            right_sums[i].sort()
        
        min_diff = float('inf')
        total_sum = sum(nums)
        
        # Iterate over all possible subset sizes in the left half
        for k in range(n + 1):
            # Corresponding subset size in the right half is n - k
            for sum_left in left_sums[k]:
                # Target sum for the right half is (total_sum / 2) - sum_left
                target = (total_sum / 2) - sum_left
                
                # Find the closest sum in right_sums[n - k]
                idx = bisect_left(right_sums[n - k], target)
                
                # Check the closest elements to the target
                if idx < len(right_sums[n - k]):
                    sum_right = right_sums[n - k][idx]
                    current_diff = abs((sum_left + sum_right) - (total_sum - (sum_left + sum_right)))
                    min_diff = min(min_diff, current_diff)
                
                if idx > 0:
                    sum_right = right_sums[n - k][idx - 1]
                    current_diff = abs((sum_left + sum_right) - (total_sum - (sum_left + sum_right)))
                    min_diff = min(min_diff, current_diff)
        
        return int(min_diff)