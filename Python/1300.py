from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def compute_sum(value):
            return sum(min(x, value) for x in arr)

        left, right = 0, max(arr)
        result = right

        while left <= right:
            mid = (left + right) // 2
            current_sum = compute_sum(mid)
            
            if current_sum < target:
                left = mid + 1
            else:
                right = mid - 1

            # Check for better result
            if abs(current_sum - target) < abs(compute_sum(result) - target):
                result = mid
            elif abs(current_sum - target) == abs(compute_sum(result) - target):
                result = min(result, mid)

        return result
