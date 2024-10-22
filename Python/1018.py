class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        current_number = 0
        
        for num in nums:
            # Update the current number by shifting left and adding the new bit
            current_number = (current_number * 2 + num) % 5
            # Check if current number is divisible by 5
            result.append(current_number == 0)
        
        return result
