from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def is_non_decreasing(nums: List[int]) -> bool:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        
        def can_be_fixed(nums: List[int], idx_to_modify: int) -> bool:
            # Try modifying nums[idx_to_modify]
            original = nums[idx_to_modify]
            nums[idx_to_modify] = nums[idx_to_modify + 1]
            if is_non_decreasing(nums):
                return True
            # Restore and try modifying nums[idx_to_modify + 1]
            nums[idx_to_modify] = original
            if idx_to_modify + 1 < len(nums):
                nums[idx_to_modify + 1] = original
                return is_non_decreasing(nums)
            return False

        violation_count = 0
        violation_index = -1

        # Detect violations
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                violation_count += 1
                violation_index = i
                if violation_count > 1:
                    return False
                break
        
        if violation_count == 0:
            return True
        
        # Try to fix the violation
        return can_be_fixed(nums, violation_index)
