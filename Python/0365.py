from math import gcd

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Get the GCD of x and y
        g = gcd(x, y)
        
        # Check if target is within the range of 0 to x + y
        return target <= x + y and target % g == 0
