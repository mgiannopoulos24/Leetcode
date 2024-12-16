class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Encode the result into the nums array
        for i in range(n):
            nums[i] += (nums[nums[i]] % n) * n
        
        # Step 2: Extract the final result by dividing each element by n
        for i in range(n):
            nums[i] //= n
        
        return nums
