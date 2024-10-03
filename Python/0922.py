class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_idx = 0  # Start with the first even index
        odd_idx = 1   # Start with the first odd index
        
        while even_idx < len(nums) and odd_idx < len(nums):
            # If the current index is even but the number is odd, swap it
            if nums[even_idx] % 2 != 0:
                # Find the next odd index with an even number
                while odd_idx < len(nums) and nums[odd_idx] % 2 != 0:
                    odd_idx += 2
                # Swap the elements
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
            
            even_idx += 2  # Move to the next even index
        
        return nums
