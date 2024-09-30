import math
from typing import List

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        
        # Function to calculate LCM
        def lcm(x: int, y: int) -> int:
            return x * y // math.gcd(x, y)
        
        # Binary search to find the nth magical number
        def countMagicalNumbers(x: int) -> int:
            countA = x // a
            countB = x // b
            countAB = x // lcm(a, b)
            return countA + countB - countAB
        
        left, right = 1, 10**18  # large number for upper bound
        
        while left < right:
            mid = (left + right) // 2
            if countMagicalNumbers(mid) < n:
                left = mid + 1
            else:
                right = mid
        
        return left % MOD
