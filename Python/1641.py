class Solution:
    def countVowelStrings(self, n: int) -> int:
        # DP approach with O(n) space
        # Initialize the base case, which is the number of strings of length 1
        dp = [1, 1, 1, 1, 1]  # These represent the number of ways to end a string with 'a', 'e', 'i', 'o', 'u'
        
        # We now build for strings of length n by updating the dp array
        for _ in range(1, n):
            for i in range(3, -1, -1):  # update dp from right to left
                dp[i] += dp[i + 1]
        
        # The result is the sum of the dp array, which represents all possible valid strings of length n
        return sum(dp)
