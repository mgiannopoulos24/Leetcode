class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            mid = (left + right) // 2
            if mid * (mid + 1) // 2 == n:
                return mid
            elif mid * (mid + 1) // 2 < n:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
