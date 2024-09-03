from math import isqrt

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        sum_divisors = 1  # Start with 1, since 1 is a divisor of every number
        
        # Find divisors from 2 up to the square root of num
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                sum_divisors += i
                if i != num // i:
                    sum_divisors += num // i
        
        return sum_divisors == num
