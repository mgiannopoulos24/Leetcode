from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        n = len(nums)
        
        if n == 0:
            return ranges
        
        start = nums[0]
        
        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                # When the current number does not continue the range
                if start == nums[i - 1]:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{nums[i - 1]}")
                # Start a new range
                start = nums[i]
        
        # Add the last range
        if start == nums[-1]:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{nums[-1]}")
        
        return ranges
