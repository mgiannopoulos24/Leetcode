from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Calculate expected sums
        expected_sum = n * (n + 1) // 2
        expected_sum_squares = n * (n + 1) * (2 * n + 1) // 6
        
        # Calculate actual sums
        sum_nums = sum(nums)
        sum_squares_nums = sum(x * x for x in nums)
        
        # Calculate differences
        diff_sum = expected_sum - sum_nums
        diff_sum_squares = expected_sum_squares - sum_squares_nums
        
        # Using the differences to find duplicated and missing numbers
        # diff_sum = missing - duplicated
        # diff_sum_squares = missing^2 - duplicated^2
        # (missing - duplicated) * (missing + duplicated) = diff_sum_squares
        
        # Solve for missing and duplicated
        missing_plus_duplicated = diff_sum_squares // diff_sum
        duplicated = (missing_plus_duplicated - diff_sum) // 2
        missing = (missing_plus_duplicated + diff_sum) // 2
        
        return [duplicated, missing]
