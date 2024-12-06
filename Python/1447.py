import math

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result = []
        
        # Iterate through all denominators from 2 to n
        for d in range(2, n + 1):
            # Iterate through all numerators less than the denominator
            for num in range(1, d):
                # Check if the gcd of numerator and denominator is 1 (i.e., it's a simplified fraction)
                if math.gcd(num, d) == 1:
                    result.append(f"{num}/{d}")
        
        return result
