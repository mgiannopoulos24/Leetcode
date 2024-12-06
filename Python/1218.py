class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}  # Dictionary to store the longest subsequence ending with each number
        max_length = 0
        
        for x in arr:
            # Check if we can extend a subsequence ending at x - difference
            if x - difference in dp:
                dp[x] = dp[x - difference] + 1
            else:
                dp[x] = 1  # Start a new subsequence with x
            
            # Track the maximum length of subsequence
            max_length = max(max_length, dp[x])
        
        return max_length
