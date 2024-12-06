MOD = 10**9 + 7

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        # Calculate the KMP failure function (prefix function) for the evil string
        def computeKMP(evil):
            m = len(evil)
            kmp = [0] * m
            j = 0  # Length of previous longest prefix suffix
            for i in range(1, m):
                while j > 0 and evil[i] != evil[j]:
                    j = kmp[j - 1]
                if evil[i] == evil[j]:
                    j += 1
                kmp[i] = j
            return kmp
        
        m = len(evil)
        kmp = computeKMP(evil)

        # DP dictionary to memoize the state transitions
        dp = {}

        def dfs(i, tight1, tight2, evilMatched):
            # Base case: we've constructed a valid string of length n
            if evilMatched == m:  # We matched the whole evil string
                return 0
            if i == n:  # If we've successfully built a string of length n
                return 1
            
            # Memoization key
            key = (i, tight1, tight2, evilMatched)
            if key in dp:
                return dp[key]
            
            # Determine the bounds for the current character
            lower = s1[i] if tight1 else 'a'
            upper = s2[i] if tight2 else 'z'
            
            # Try all valid characters in the range [lower, upper]
            result = 0
            for char in range(ord(lower), ord(upper) + 1):
                c = chr(char)
                j = evilMatched
                # Update the evilMatched state using KMP-like transitions
                while j > 0 and c != evil[j]:
                    j = kmp[j - 1]
                if c == evil[j]:
                    j += 1
                
                # Recursively count all valid strings
                result += dfs(i + 1,
                              tight1 and (c == lower),
                              tight2 and (c == upper),
                              j)
                result %= MOD

            dp[key] = result
            return result

        return dfs(0, True, True, 0)
