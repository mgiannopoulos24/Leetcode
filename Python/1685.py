class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        # Step 1: Compute the prefix sum of nums
        total_sum = sum(nums)
        prefix_sum = 0
        
        for i in range(n):
            # Contribution of the elements on the left of nums[i]
            if i > 0:
                prefix_sum += nums[i-1]
                
            left_sum = i * nums[i] - prefix_sum
            
            # Contribution of the elements on the right of nums[i]
            right_sum = (total_sum - prefix_sum - nums[i]) - (n - i - 1) * nums[i]
            
            # Store the result for nums[i]
            result[i] = left_sum + right_sum
        
        return result
