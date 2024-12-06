class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calculate_sum(x, length):
            if x > length:
                return (x + (x - length + 1)) * length // 2
            else:
                return (x * (x + 1)) // 2 + (length - x)
        
        left_length = index
        right_length = n - index - 1
        low, high = 1, maxSum

        while low < high:
            mid = (low + high + 1) // 2
            total = mid + calculate_sum(mid - 1, left_length) + calculate_sum(mid - 1, right_length)
            
            if total <= maxSum:
                low = mid
            else:
                high = mid - 1
        
        return low
