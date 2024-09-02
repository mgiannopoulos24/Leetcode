class Solution:
    def integerReplacement(self, n: int) -> int:
        operations = 0
        
        while n > 1:
            if n % 2 == 0:
                # If n is even, divide by 2
                n //= 2
            else:
                # If n is odd, choose between n + 1 or n - 1
                # Check if n is 3, then the best operation is to subtract 1
                if n == 3:
                    n -= 1
                else:
                    # We use the bitwise operations to determine the optimal choice
                    if (n & 2) == 0 or (n == 1):
                        n -= 1
                    else:
                        n += 1
            operations += 1
        
        return operations
