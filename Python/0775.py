class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # Traverse the list and check the condition
        for i in range(len(nums)):
            # Check if the current element is more than 1 position away from its index
            if abs(nums[i] - i) > 1:
                return False
        return True
