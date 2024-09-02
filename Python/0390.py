class Solution:
    def lastRemaining(self, n: int) -> int:
        step = 1  # Step size
        start = 1  # Starting position
        remaining = n
        left_to_right = True  # Direction flag
        
        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                start += step  # Update start position if direction is left-to-right or if remaining is odd
            step *= 2  # Double the step size
            remaining //= 2  # Halve the number of remaining elements
            left_to_right = not left_to_right  # Alternate direction
        
        return start
