class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        
        # List to store all subarray sums
        subarray_sums = []
        
        # Generate all subarray sums
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
        
        # Sort the subarray sums
        subarray_sums.sort()
        
        # Calculate the sum of subarray sums from index `left-1` to `right-1`
        return sum(subarray_sums[left-1:right]) % MOD
