class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Kadane's algorithm to find maximum subarray sum
        def kadane(arr):
            max_sum = 0
            current_sum = 0
            for num in arr:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum
        
        # Find the sum of the entire array
        total_sum = sum(arr)
        
        # Case 1: kadane(arr) for k = 1
        kadane_one = kadane(arr)
        
        if k == 1:
            return kadane_one % MOD
        
        # Find the maximum prefix sum
        prefix_sum = 0
        max_prefix_sum = 0
        for num in arr:
            prefix_sum += num
            max_prefix_sum = max(max_prefix_sum, prefix_sum)
        
        # Find the maximum suffix sum
        suffix_sum = 0
        max_suffix_sum = 0
        for num in reversed(arr):
            suffix_sum += num
            max_suffix_sum = max(max_suffix_sum, suffix_sum)
        
        # Case 2: k = 2, kadane(arr) or span across two arrays (suffix + prefix)
        max_double_kadane = max(kadane_one, max_suffix_sum + max_prefix_sum)
        
        if k == 2:
            return max_double_kadane % MOD
        
        # Case 3: k > 2, combine prefix, suffix, and whole array sums
        if total_sum > 0:
            result = max(max_double_kadane, max_suffix_sum + max_prefix_sum + (k - 2) * total_sum)
        else:
            result = max_double_kadane
        
        return result % MOD
