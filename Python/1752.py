from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        break_count = 0
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                break_count += 1
            if break_count > 1:
                return False
        
        return True
