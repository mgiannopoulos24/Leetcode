class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_position = -1  # To store the position of the last seen 1
        
        for i, num in enumerate(nums):
            if num == 1:
                if last_position != -1 and i - last_position - 1 < k:
                    return False  # The distance between two 1's is less than k
                last_position = i  # Update the position of the last seen 1
        
        return True