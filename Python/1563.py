class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == j:
                return 0
            maxi = 0
            total = prefix[j + 1] - prefix[i]  # Total sum of the current subarray
            for k in range(i, j):
                left = prefix[k + 1] - prefix[i]  # Sum of the left partition
                right = total - left  # Sum of the right partition
                if left < right:
                    if left + dp(i, k) > maxi:
                        maxi = left + dp(i, k)
                elif left > right:
                    if right + dp(k + 1, j) > maxi:
                        maxi = right + dp(k + 1, j)
                else:
                    # If left == right, choose the maximum of the two branches
                    current_max = left + max(dp(i, k), dp(k + 1, j))
                    if current_max > maxi:
                        maxi = current_max
            return maxi

        return dp(0, n - 1)