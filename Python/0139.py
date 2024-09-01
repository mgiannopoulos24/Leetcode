from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert the wordDict into a set for O(1) look-up times
        word_set = set(wordDict)
        
        # Initialize the DP array
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: an empty string can be segmented
        
        # Fill the DP array
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further if dp[i] is True
        
        return dp[len(s)]
