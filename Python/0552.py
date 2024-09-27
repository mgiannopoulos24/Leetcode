MOD = 10**9 + 7

class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3  # "P", "L", "A"
        
        # dp_no_A[i]: valid sequences of length i without any 'A'
        dp_no_A = [0] * (n + 1)
        
        # Base cases
        dp_no_A[0] = 1  # Empty record
        dp_no_A[1] = 2  # "P", "L"
        dp_no_A[2] = 4  # "PP", "PL", "LP", "LL"

        # Fill dp_no_A using recurrence
        for i in range(3, n + 1):
            dp_no_A[i] = (dp_no_A[i-1] + dp_no_A[i-2] + dp_no_A[i-3]) % MOD
        
        # Now calculate the total number of valid sequences, including exactly one 'A'
        total = dp_no_A[n]  # All records with no 'A'

        # Consider placing 'A' in every possible position (i.e., split into two parts)
        for i in range(1, n + 1):
            left = dp_no_A[i-1]  # Valid records of length i-1 without 'A'
            right = dp_no_A[n-i]  # Valid records of length n-i without 'A'
            total = (total + left * right) % MOD

        return total
