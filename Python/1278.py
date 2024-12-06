from typing import List
from functools import lru_cache

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        if k > n:
            return -1  # Not enough characters to form k substrings

        # Precompute the cost to make any substring s[i..j] a palindrome
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                cnt = 0
                left, right = i, j
                while left < right:
                    if s[left] != s[right]:
                        cnt += 1
                    left += 1
                    right -= 1
                cost[i][j] = cnt

        # Define the DP function with memoization
        @lru_cache(maxsize=None)
        def dp(pos: int, cnt: int) -> int:
            # Base Cases
            if cnt == 0 and pos == n:
                return 0
            if cnt == 0 or pos == n:
                return float('inf')
            if n - pos < cnt:
                return float('inf')  # Not enough characters to form cnt substrings

            min_changes = float('inf')
            # Try all possible end indices for the current substring
            for i in range(pos, n - cnt + 1):
                current_cost = cost[pos][i]
                rest_cost = dp(i + 1, cnt - 1)
                if rest_cost != float('inf'):
                    min_changes = min(min_changes, current_cost + rest_cost)
            return min_changes

        result = dp(0, k)
        return result if result != float('inf') else -1
