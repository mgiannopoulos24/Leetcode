class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        
        # Helper function to compute the length of the compressed form of a count
        def get_compressed_length(count):
            if count == 1:
                return 1  # just the character
            elif count < 10:
                return 2  # character + 1 digit
            elif count < 100:
                return 3  # character + 2 digits
            else:
                return 4  # character + 3 digits
        
        # DP table: dp[i][k] represents the minimum length for substring s[i:] with at most k deletions
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        
        # Base case: no characters left means compressed length is 0
        dp[n] = [0] * (k + 1)
        
        # Fill the DP table from the back to the front
        for i in range(n - 1, -1, -1):
            for rem_k in range(k + 1):
                count = 0
                deletions_used = 0
                
                # Consider all consecutive groups of the same character starting from s[i]
                for j in range(i, n):
                    if s[i] == s[j]:
                        count += 1  # we found another same character
                    else:
                        deletions_used += 1  # we may consider deleting this character
                        
                    if deletions_used > rem_k:
                        break
                    
                    # Calculate compressed length for this group
                    compressed_len = get_compressed_length(count)
                    dp[i][rem_k] = min(dp[i][rem_k], compressed_len + dp[j + 1][rem_k - deletions_used])
                
                # Option 2: delete the current character
                dp[i][rem_k] = min(dp[i][rem_k], dp[i + 1][rem_k - 1] if rem_k > 0 else float('inf'))
        
        return dp[0][k]
