class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        # Check the conditions
        if total_xor == 0:
            return True
        else:
            # Alice wins if the number of elements is even
            return len(nums) % 2 == 0
