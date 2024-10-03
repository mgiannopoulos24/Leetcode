class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        # Prefix sums for the number of 1s up to each index
        prefix1 = [0] * (n + 1)
        # Suffix sums for the number of 0s from each index
        suffix0 = [0] * (n + 1)
        
        # Fill prefix1 where prefix1[i] is the number of 1s in s[:i]
        for i in range(1, n + 1):
            prefix1[i] = prefix1[i - 1] + (s[i - 1] == '1')
        
        # Fill suffix0 where suffix0[i] is the number of 0s in s[i:]
        for i in range(n - 1, -1, -1):
            suffix0[i] = suffix0[i + 1] + (s[i] == '0')
        
        # Calculate the minimum flips required
        min_flips = float('inf')
        for i in range(n + 1):
            min_flips = min(min_flips, prefix1[i] + suffix0[i])
        
        return min_flips
