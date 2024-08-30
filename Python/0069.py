class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # Directly return x for 0 and 1

        left, right = 0, x
        
        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid
            
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # After the loop, `right` will be the largest integer whose square is <= x
        return right