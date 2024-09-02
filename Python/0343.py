class Solution:
    def integerBreak(self, n: int) -> int:
        # Handle the simple cases directly
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        # For n >= 4
        product = 1
        
        while n > 4:
            product *= 3
            n -= 3
        
        product *= n
        return product
