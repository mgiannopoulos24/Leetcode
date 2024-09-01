from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find the median
        median = self.findMedian(nums)
        
        # Step 2: Partition the array into smaller and larger than the median
        numsCopy = nums[:]
        index = 0
        for num in numsCopy:
            if num < median:
                nums[index] = num
                index += 1
        for num in numsCopy:
            if num == median:
                nums[index] = num
                index += 1
        for num in numsCopy:
            if num > median:
                nums[index] = num
                index += 1
        
        # Step 3: Rearrange elements to fit the wiggle pattern
        result = [0] * n
        mid = (n + 1) // 2
        left = mid - 1
        right = n - 1
        
        for i in range(n):
            if i % 2 == 0:
                result[i] = nums[left]
                left -= 1
            else:
                result[i] = nums[right]
                right -= 1
        
        nums[:] = result

    def findMedian(self, nums: List[int]) -> int:
        numsCopy = nums[:]
        numsCopy.sort()
        return numsCopy[len(nums) // 2]
