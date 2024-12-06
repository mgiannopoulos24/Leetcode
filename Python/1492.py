class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        
        # Loop through 1 to sqrt(n) to find factors
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:  # i is a factor
                factors.append(i)
                if i != n // i:  # Ensure the other factor n // i is distinct
                    factors.append(n // i)
        
        # Sort factors to ensure ascending order
        factors.sort()
        
        # Check if there are at least k factors
        if len(factors) >= k:
            return factors[k - 1]  # Return the k-th factor
        else:
            return -1  # If fewer than k factors
