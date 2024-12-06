class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initialize dp arrays for the current and previous rows
        dp_prev = [1] * 5  # For strings of length 1, each vowel can be used once
        
        for i in range(2, n + 1):
            dp_curr = [0] * 5  # Temporary array for the current row
            
            # Apply the recurrence relations based on the problem statement
            dp_curr[0] = dp_prev[1]  # 'a' can only come from 'e'
            dp_curr[1] = (dp_prev[0] + dp_prev[2]) % MOD  # 'e' can come from 'a' and 'i'
            dp_curr[2] = (dp_prev[0] + dp_prev[1] + dp_prev[3] + dp_prev[4]) % MOD  # 'i' can come from 'a', 'e', 'o', 'u'
            dp_curr[3] = (dp_prev[2] + dp_prev[4]) % MOD  # 'o' can come from 'i' and 'u'
            dp_curr[4] = dp_prev[0]  # 'u' can only come from 'a'
            
            # Move to the next state
            dp_prev = dp_curr
        
        # Sum of all the vowel-ending strings of length n
        return sum(dp_prev) % MOD
