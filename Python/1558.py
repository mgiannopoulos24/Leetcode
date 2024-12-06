class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Initialize counts
        max_double_ops = 0  # This will track the maximum number of doubling operations needed
        total_increments = 0  # This will track the total number of increment operations needed
        
        for num in nums:
            current_double_ops = 0
            while num > 0:
                if num % 2 == 1:  # If the current bit is 1, we need an increment
                    total_increments += 1
                num //= 2  # This simulates the doubling operation in reverse (bit shifting)
                current_double_ops += 1
            
            # Update max_double_ops for the largest number
            max_double_ops = max(max_double_ops, current_double_ops - 1)  # subtract 1 since final state doesn't require doubling
        
        # The total operations are the sum of all increments and the max double operations
        return total_increments + max_double_ops
