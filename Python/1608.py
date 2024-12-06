class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Iterate over all possible values of x
        for x in range(len(nums) + 1):
            # Count how many numbers are greater than or equal to x
            count = sum(1 for num in nums if num >= x)
            # Check if the count matches the value of x
            if count == x:
                return x
        # If no special value x is found, return -1
        return -1
