class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        nums.sort(reverse=True)  # Sort in descending order for optimization
        
        # If the largest number is greater than the target sum, it's not possible to partition
        if nums[0] > target:
            return False
        
        n = len(nums)
        used = [False] * n
        
        def can_form_subset(index, current_sum, count):
            if count == k - 1:  # If we formed k-1 subsets, the remaining elements form the last subset
                return True
            if current_sum == target:  # Found a valid subset
                return can_form_subset(0, 0, count + 1)
            for i in range(index, n):
                if not used[i] and current_sum + nums[i] <= target:
                    used[i] = True
                    if can_form_subset(i + 1, current_sum + nums[i], count):
                        return True
                    used[i] = False
            return False
        
        return can_form_subset(0, 0, 0)
