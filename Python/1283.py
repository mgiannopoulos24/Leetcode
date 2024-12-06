class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Helper function to calculate the sum of divisions
        def compute_sum(divisor):
            total = 0
            for num in nums:
                total += (num + divisor - 1) // divisor  # This is equivalent to math.ceil(num / divisor)
            return total
        
        # Binary search for the smallest divisor
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if compute_sum(mid) > threshold:
                left = mid + 1  # Mid is too small, we need a larger divisor
            else:
                right = mid  # Mid might be a valid answer, so we look for a smaller one
        
        return left
