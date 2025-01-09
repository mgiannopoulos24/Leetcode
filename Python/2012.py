class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_max = [0] * n
        suffix_min = [0] * n
        
        # Compute prefix_max
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i-1])
        
        # Compute suffix_min
        suffix_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i+1])
        
        beauty_sum = 0
        for i in range(1, n-1):
            if prefix_max[i] < nums[i] < suffix_min[i]:
                beauty_sum += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                beauty_sum += 1
        
        return beauty_sum