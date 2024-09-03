from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
            else:
                if current_count > max_count:
                    max_count = current_count
                current_count = 0
        
        # Final check to update max_count in case the longest streak ends at the end
        if current_count > max_count:
            max_count = current_count
        
        return max_count