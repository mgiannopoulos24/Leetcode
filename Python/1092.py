class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Step 1: Find the LCS using dynamic programming
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the dp table for LCS
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Step 2: Construct the shortest common supersequence
        result = []
        i, j = m, n
        
        # Trace the LCS backwards to build the SCS
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                # If the characters match, they must be part of the SCS
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                # Prefer str1 if there's a choice, append from str1
                result.append(str1[i - 1])
                i -= 1
            else:
                # Otherwise append from str2
                result.append(str2[j - 1])
                j -= 1
        
        # Add remaining characters from str1 or str2
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        while j > 0:
            result.append(str2[j - 1])
            j -= 1
        
        # The result is built backwards, so reverse it
        return ''.join(reversed(result))
