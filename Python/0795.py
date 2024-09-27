class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_subarrays_with_max_less_equal(x: int) -> int:
            count = 0
            start = 0
            for end in range(len(nums)):
                if nums[end] > x:
                    start = end + 1
                count += end - start + 1
            return count
        
        # Calculate the number of subarrays with max ≤ right
        count_max_le_right = count_subarrays_with_max_less_equal(right)
        # Calculate the number of subarrays with max ≤ left - 1
        count_max_le_left_minus_1 = count_subarrays_with_max_less_equal(left - 1)
        
        # The desired count is the difference between the two counts
        return count_max_le_right - count_max_le_left_minus_1
