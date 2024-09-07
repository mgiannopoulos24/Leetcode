from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        # Iterate from the end of the sorted list for the largest side
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # If nums[i] + nums[j] > nums[k], all elements from i to j are valid
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
                    
        return count
