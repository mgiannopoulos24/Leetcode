from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize the binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        # Perform binary search on the smaller array nums1
        while low <= high:
            partition1 = (low + high) // 2  # Calculate partition for nums1
            partition2 = (m + n + 1) // 2 - partition1  # Calculate partition for nums2
            
            # Determine the elements around partitions for both arrays
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if partitions are correct for median condition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total length is even, return average of middle elements
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    # If total length is odd, return the larger of the two middle elements
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                # Adjust partition1 to the left if maxLeft1 is too large
                high = partition1 - 1
            else:
                # Adjust partition1 to the right if maxLeft2 is too large
                low = partition1 + 1
        
        # If input arrays are not sorted (though they should be), raise an error
        raise ValueError("Input arrays are not sorted")
