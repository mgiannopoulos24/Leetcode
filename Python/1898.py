from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def canMakeSubsequence(k: int) -> bool:
            removed = [False] * len(s)
            # Mark the first k removals
            for i in range(k):
                removed[removable[i]] = True
            
            # Try to match p with s while skipping removed characters
            i, j = 0, 0  # i for s, j for p
            while i < len(s) and j < len(p):
                if not removed[i] and s[i] == p[j]:
                    j += 1
                i += 1
            
            return j == len(p)
        
        # Binary search on the number of removals
        left, right = 0, len(removable)
        while left < right:
            mid = (left + right + 1) // 2  # Try to check the middle point
            if canMakeSubsequence(mid):
                left = mid  # Try for a larger k
            else:
                right = mid - 1  # Try for a smaller k
        
        return left
