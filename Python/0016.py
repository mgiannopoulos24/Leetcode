class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array
        n = len(nums)
        closest_sum = float('inf')  # Initialize with a large number
        min_diff = float('inf')     # Initialize with a large number
        
        for i in range(n - 2):
            left, right = i + 1, n - 1  # Two pointers
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                diff = abs(current_sum - target)
                
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target  # Exact match found, return early
        
        return closest_sum