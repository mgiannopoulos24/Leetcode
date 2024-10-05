from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0

        n = len(strs)
        m = len(strs[0])
        
        # Initialize DP array where DP[i] is the max number of kept columns up to i
        DP = [1] * m
        
        for i in range(m):
            for j in range(i):
                # Check if column i can be appended after column j
                can_append = True
                for k in range(n):
                    if strs[k][i] < strs[k][j]:
                        can_append = False
                        break
                if can_append:
                    DP[i] = max(DP[i], DP[j] + 1)
        
        max_kept = max(DP)
        return m - max_kept
