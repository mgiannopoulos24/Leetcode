class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        # Function to calculate permutations P(a, b)
        def permutations(a, b):
            result = 1
            for i in range(b):
                result *= (a - i)
            return result
        
        # Count unique digit numbers of length 1 to n
        total_count = 0
        for length in range(1, n + 1):
            if length == 1:
                # For 1-digit numbers, we have digits 0 through 9
                total_count += 10
            else:
                # For length > 1, use the permutations formula
                count = 9 * permutations(9, length - 1)
                total_count += count
        
        return total_count
