class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeftmostIndex(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def findRightmostIndex(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left_idx = findLeftmostIndex(nums, target)
        right_idx = findRightmostIndex(nums, target)
        
        if left_idx <= right_idx and nums[left_idx] == target:
            return [left_idx, right_idx]
        else:
            return [-1, -1]
