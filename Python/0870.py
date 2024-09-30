class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()
        sorted_nums2 = sorted([(val, idx) for idx, val in enumerate(nums2)], reverse=True)
        res = [0]*n
        left, right = 0, n-1

        for val2, idx in sorted_nums2:
            if nums1[right] > val2:
                res[idx] = nums1[right]
                right -=1
            else:
                res[idx] = nums1[left]
                left +=1

        return res
