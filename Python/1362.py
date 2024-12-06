import math

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        # Helper function to find the closest divisors for a given number
        def find_closest_divisors(n):
            for i in range(int(math.sqrt(n)), 0, -1):
                if n % i == 0:
                    return [i, n // i]
            return []
        
        # Check divisors for num + 1
        divisors1 = find_closest_divisors(num + 1)
        # Check divisors for num + 2
        divisors2 = find_closest_divisors(num + 2)
        
        # Compare the two pairs of divisors and return the one with the smallest difference
        if abs(divisors1[0] - divisors1[1]) < abs(divisors2[0] - divisors2[1]):
            return divisors1
        else:
            return divisors2
