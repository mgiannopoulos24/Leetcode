import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        # Precompute all squares up to n^2
        squares = set(i * i for i in range(1, n + 1))
        
        # Iterate over all pairs (a, b)
        for a in range(1, n + 1):
            for b in range(a, n + 1):  # To avoid double counting (a,b) and (b,a)
                sum_of_squares = a * a + b * b
                # Check if sum_of_squares is a perfect square and <= n^2
                if sum_of_squares in squares:
                    # Get the corresponding value of c
                    c = int(math.sqrt(sum_of_squares))
                    # If c is valid, count the pair
                    if c <= n:
                        # If a != b, we count both (a, b, c) and (b, a, c)
                        if a != b:
                            count += 2
                        else:
                            count += 1
        return count
