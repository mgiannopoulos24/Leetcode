from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # Calculate the sums of nums1 and nums2
        sum1, sum2 = sum(nums1), sum(nums2)
        
        # If sums are already equal, no operations are needed
        if sum1 == sum2:
            return 0
        
        # Make sum1 always the larger one for consistency in handling the diff
        if sum1 < sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1
        
        # Calculate the difference that needs to be reduced
        diff = sum1 - sum2
        
        # Gather potential decreases in nums1 and potential increases in nums2
        changes = []
        for num in nums1:
            changes.append(num - 1)  # Max decrease for each element in nums1
        for num in nums2:
            changes.append(6 - num)  # Max increase for each element in nums2
        
        # Sort changes in descending order to maximize impact
        changes.sort(reverse=True)
        
        # Apply the changes greedily
        operations = 0
        for change in changes:
            diff -= change
            operations += 1
            if diff <= 0:
                return operations
        
        # If we exhausted all changes and still have non-zero difference, return -1
        return -1
