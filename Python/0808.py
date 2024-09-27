from functools import lru_cache

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1.0  # For large n, the probability converges to 1.0

        @lru_cache(None)
        def dp(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            prob = 0.25 * (dp(max(0, a - 100), b) +
                           dp(max(0, a - 75), max(0, b - 25)) +
                           dp(max(0, a - 50), max(0, b - 50)) +
                           dp(max(0, a - 25), max(0, b - 75)))
            return prob
        
        return dp(n, n)
