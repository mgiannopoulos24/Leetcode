class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Initialize the DP arrays
        lengths = [1] * n  # lengths[i] will store the length of the longest subsequence ending at i
        counts = [1] * n   # counts[i] will store the number of longest subsequences ending at i
        
        # Fill the DP arrays
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # If a longer subsequence can be formed by appending nums[i] to nums[j]
                    if lengths[i] < lengths[j] + 1:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[i] == lengths[j] + 1:
                        counts[i] += counts[j]
        
        # Find the length of the longest increasing subsequence
        max_length = max(lengths)
        
        # Sum up the number of longest increasing subsequences
        return sum(counts[i] for i in range(n) if lengths[i] == max_length)
