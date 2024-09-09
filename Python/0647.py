class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        total_count = 0
        for i in range(len(s)):
            # Count odd-length palindromes
            total_count += expandAroundCenter(i, i)
            # Count even-length palindromes
            total_count += expandAroundCenter(i, i + 1)
        
        return total_count
