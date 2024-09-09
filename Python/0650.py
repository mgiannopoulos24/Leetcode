class Solution:
    def minSteps(self, n: int) -> int:
        steps = 0
        # Start with the smallest prime factor
        factor = 2
        
        # Factorize n
        while factor * factor <= n:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1
        
        # If n is still greater than 1, then it is a prime number
        if n > 1:
            steps += n
        
        return steps
