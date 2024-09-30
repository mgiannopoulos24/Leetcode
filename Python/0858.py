import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Find the least common multiple of p and q
        lcm = (p * q) // math.gcd(p, q)
        
        # Number of horizontal reflections (on east-west walls)
        k = lcm // p
        # Number of vertical reflections (on north-south walls)
        m = lcm // q
        
        # Determine the receptor based on the parity of k and m
        if k % 2 == 0 and m % 2 == 1:
            return 0  # Hits receptor 0
        elif k % 2 == 1 and m % 2 == 1:
            return 1  # Hits receptor 1
        else:
            return 2  # Hits receptor 2
