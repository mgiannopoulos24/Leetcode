# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2  # To prevent potential overflow
            if isBadVersion(mid):
                right = mid  # First bad version is at mid or before
            else:
                left = mid + 1  # First bad version is after mid
        
        # When left == right, it is the first bad version
        return left