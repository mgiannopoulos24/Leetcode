class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return 2  # If there are only two numbers, the answer is 2.

        # Initialize a list of dictionaries to track the length of arithmetic sequences for each index.
        dp = [{} for _ in range(n)]
        max_length = 2  # At least two numbers form an arithmetic sequence.
        
        # Loop over each pair of numbers to compute differences
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                # If there is already a sequence ending at j with this difference, extend it
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2  # Start a new sequence with length 2
                
                # Update the global maximum length
                max_length = max(max_length, dp[i][diff])
        
        return max_length
