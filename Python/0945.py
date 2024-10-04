class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # Sort the array
        nums.sort()
        
        # Initialize the number of moves and the last unique number
        moves = 0
        last_unique = nums[0]
        
        # Iterate through the sorted array
        for i in range(1, len(nums)):
            if nums[i] <= last_unique:
                # If the current number is not unique, increment it
                moves += last_unique + 1 - nums[i]
                last_unique += 1
            else:
                # Update the last unique number
                last_unique = nums[i]
        
        return moves
