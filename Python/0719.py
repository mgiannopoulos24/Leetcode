from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def countPairsLessThanOrEqualTo(d: int) -> int:
            count = 0
            start = 0
            for end in range(len(nums)):
                while nums[end] - nums[start] > d:
                    start += 1
                count += (end - start)
            return count
        
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            if countPairsLessThanOrEqualTo(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left
