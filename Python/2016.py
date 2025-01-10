class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = nums[0]  # Initialize the minimum number
        max_diff = -1      # Initialize the maximum difference

        for num in nums[1:]:
            if num > min_num:
                # Update the maximum difference if the current difference is greater
                max_diff = max(max_diff, num - min_num)
            else:
                # Update the minimum number if the current number is smaller
                min_num = min(min_num, num)

        return max_diff