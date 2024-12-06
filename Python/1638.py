class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        result = 0
        
        # Helper function to count valid substrings differing by exactly 1 character
        def count_diff_by_one(i, j):
            count = 0
            diff = 0
            while i < m and j < n:
                if s[i] != t[j]:
                    diff += 1
                if diff == 1:
                    count += 1
                elif diff > 1:
                    break
                i += 1
                j += 1
            return count
        
        # Compare substrings starting from each position in s and t
        for i in range(m):
            for j in range(n):
                result += count_diff_by_one(i, j)
        
        return result
