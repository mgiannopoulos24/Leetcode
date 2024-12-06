class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            # Insert nums[i] at index[i] in the target array
            target.insert(index[i], nums[i])
        return target
