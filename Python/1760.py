from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canAchievePenalty(penalty):
            operations_needed = 0
            for balls in nums:
                if balls > penalty:
                    # Calculate the number of operations required for this bag
                    operations_needed += (balls - 1) // penalty
                if operations_needed > maxOperations:
                    return False
            return operations_needed <= maxOperations

        # Binary search on the possible penalty values
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canAchievePenalty(mid):
                right = mid  # Try a smaller penalty
            else:
                left = mid + 1  # Increase the penalty

        return left
