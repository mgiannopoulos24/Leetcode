class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        i, j, k = 0, 1, 0
        
        while j + k < n:
            if s[i + k] == s[j + k]:
                # Characters at current offset are the same, move further
                k += 1
            elif s[i + k] > s[j + k]:
                # s[i+k] > s[j+k], so j is not a better suffix, move j to the next candidate
                j = j + k + 1
                k = 0  # Reset k because we are starting fresh from the new j
            else:
                # s[j+k] > s[i+k], so j is the better suffix, move i to j
                i = max(i + k + 1, j)
                j = i + 1  # Move j to be the next index after the new i
                k = 0  # Reset k because we are starting fresh
        
        # Return the largest suffix starting at i
        return s[i:]
