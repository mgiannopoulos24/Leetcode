class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Compute LIS (Longest Increasing Subsequence) for each index
        lis = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        
        # Step 2: Compute LDS (Longest Decreasing Subsequence) for each index
        lds = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)
        
        # Step 3: Find the maximum length of mountain array
        max_mountain_length = 0
        for i in range(1, n - 1):
            if lis[i] >= 2 and lds[i] >= 2:  # A valid peak should have both LIS and LDS >= 2
                max_mountain_length = max(max_mountain_length, lis[i] + lds[i] - 1)
        
        # Step 4: Minimum removals to make the array a mountain array
        return n - max_mountain_length
