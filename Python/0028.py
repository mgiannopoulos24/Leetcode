from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # Constructing prefix table for needle
        def buildPrefixTable(pattern: str) -> List[int]:
            n = len(pattern)
            prefix = [0] * n
            j = 0
            
            for i in range(1, n):
                while j > 0 and pattern[i] != pattern[j]:
                    j = prefix[j - 1]
                
                if pattern[i] == pattern[j]:
                    j += 1
                    prefix[i] = j
            
            return prefix
        
        # KMP algorithm to search for needle in haystack
        m, n = len(haystack), len(needle)
        if n > m:
            return -1
        
        prefix = buildPrefixTable(needle)
        i, j = 0, 0
        
        while i < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == n:
                    return i - n
            else:
                if j > 0:
                    j = prefix[j - 1]
                else:
                    i += 1
        
        return -1
