import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = int(math.log2(n)) + 1
        
        for m in range(max_m, 1, -1):
            # Binary search for k
            left, right = 2, int(n**0.5) + 1
            while left <= right:
                mid = (left + right) // 2
                power = mid**m
                sum_ = (power - 1) // (mid - 1)
                
                if sum_ == n:
                    return str(mid)
                elif sum_ < n:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return str(n - 1)
