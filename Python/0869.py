from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Helper function to compute the digit count
        def digit_count(x):
            return Counter(str(x))
        
        # Calculate the digit count of the given number n
        n_digit_count = digit_count(n)
        
        # Compare this digit count with all powers of 2 up to 10^9
        for i in range(31):
            power_of_2 = 1 << i  # This is 2^i
            if digit_count(power_of_2) == n_digit_count:
                return True
        
        return False
