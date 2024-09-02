from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum: int) -> bool:
            current_sum = 0
            required_subarrays = 1  # Start with one subarray
            
            for num in nums:
                if current_sum + num > max_sum:
                    required_subarrays += 1
                    current_sum = num
                    if required_subarrays > k:
                        return False
                else:
                    current_sum += num
            
            return True
        
        # Binary search for the smallest maximum subarray sum
        low, high = max(nums), sum(nums)
        
        while low < high:
            mid = (low + high) // 2
            if can_split(mid):
                high = mid
            else:
                low = mid + 1
        
        return low