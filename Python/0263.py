class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # Define a list of prime factors we are interested in
        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime
        
        # If n is reduced to 1, it means it was only composed of 2, 3, and 5
        return n == 1
