class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        current_sum = 0
        min_sum = 0  # This will track the minimum value of current_sum
        
        # Iterate over the array
        for num in nums:
            current_sum += num
            min_sum = min(min_sum, current_sum)
        
        # The minimum start value should ensure current_sum >= 1 at all times
        return 1 - min_sum if min_sum < 0 else 1