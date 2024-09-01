from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maxSingleNumber(nums: List[int], k: int) -> List[int]:
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(nums1: List[int], nums2: List[int]) -> List[int]:
            result = []
            while nums1 or nums2:
                if nums1 > nums2:
                    result.append(nums1.pop(0))
                else:
                    result.append(nums2.pop(0))
            return result

        max_number = []
        # Iterate through all possible splits
        for i in range(max(0, k - len(nums2)), min(len(nums1), k) + 1):
            part1 = maxSingleNumber(nums1, i)
            part2 = maxSingleNumber(nums2, k - i)
            merged = merge(part1, part2)
            max_number = max(max_number, merged)

        return max_number
