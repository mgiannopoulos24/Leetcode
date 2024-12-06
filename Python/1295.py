class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Initialize the count for numbers with even digits
        count = 0
        
        # Iterate through each number in the list
        for num in nums:
            # Convert the number to a string and check its length
            if len(str(num)) % 2 == 0:
                count += 1
        
        # Return the total count of numbers with even number of digits
        return count
