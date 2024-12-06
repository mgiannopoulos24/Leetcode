class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        i, j = 0, 0
        sum1, sum2 = 0, 0  # Sums for paths in nums1 and nums2
        result = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                # Encounter a common element, choose the maximum sum path
                result += max(sum1, sum2) + nums1[i]
                result %= MOD
                sum1, sum2 = 0, 0
                i += 1
                j += 1
        
        # Add remaining elements from nums1 (if any)
        while i < len(nums1):
            sum1 += nums1[i]
            i += 1
        
        # Add remaining elements from nums2 (if any)
        while j < len(nums2):
            sum2 += nums2[j]
            j += 1
        
        # Add the maximum of the remaining sums
        result += max(sum1, sum2)
        result %= MOD
        
        return result
