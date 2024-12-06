from typing import List

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        # The maximum position we need to consider is min(steps, arrLen -1)
        max_pos = min(steps, arrLen -1)
        
        # Initialize previous and current DP arrays
        prev = [0] * (max_pos + 2)  # +2 to handle pos+1 without index error
        prev[0] = 1  # Starting at position 0 with 0 steps
        
        for step in range(1, steps +1):
            curr_max_pos = min(step, max_pos)
            curr = [0] * (max_pos +2)
            for pos in range(0, curr_max_pos +1):
                # Stay
                curr[pos] = (curr[pos] + prev[pos]) % MOD
                # Move Left (from pos +1 to pos)
                if pos +1 <= max_pos:
                    curr[pos] = (curr[pos] + prev[pos +1]) % MOD
                # Move Right (from pos -1 to pos)
                if pos -1 >=0:
                    curr[pos] = (curr[pos] + prev[pos -1]) % MOD
            prev = curr
        
        return prev[0]
