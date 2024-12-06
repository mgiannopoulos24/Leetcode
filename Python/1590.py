class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target_remainder = total_sum % p
        
        # If the total sum is already divisible by p, return 0
        if target_remainder == 0:
            return 0
        
        # Dictionary to store the last occurrence of a particular remainder
        prefix_remainders = {0: -1}
        current_sum = 0
        min_length = len(nums)
        
        for i, num in enumerate(nums):
            current_sum += num
            remainder = current_sum % p
            
            # We need to find if we have seen (current_remainder - target_remainder) % p before
            needed_remainder = (remainder - target_remainder) % p
            
            if needed_remainder in prefix_remainders:
                # Check the length of the subarray that could be removed
                min_length = min(min_length, i - prefix_remainders[needed_remainder])
            
            # Update the last occurrence of this remainder
            prefix_remainders[remainder] = i
        
        # If we found a valid subarray, return its length, otherwise return -1
        return min_length if min_length < len(nums) else -1
