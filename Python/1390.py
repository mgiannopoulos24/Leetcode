import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def find_divisors(num):
            divisors = set()
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    if i != num // i:
                        divisors.add(num // i)
                if len(divisors) > 4:
                    return 0  # Early exit if more than 4 divisors
            if len(divisors) == 4:
                return sum(divisors)
            return 0
        
        total_sum = 0
        for num in nums:
            total_sum += find_divisors(num)
        
        return total_sum
