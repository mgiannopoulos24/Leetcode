class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        max_dist = 0

        for j in range(len(nums2)):
            while i < len(nums1) and nums1[i] > nums2[j]:
                i += 1
            if i < len(nums1):
                max_dist = max(max_dist, j - i)

        return max_dist
