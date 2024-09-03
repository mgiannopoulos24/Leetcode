from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        else:
            # Construct the optimal division string
            # Start with the first number
            result = str(nums[0]) + "/("
            # Append the remaining numbers separated by '/'
            result += "/".join(map(str, nums[1:]))
            # Close the parentheses
            result += ")"
            return result
