from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Helper function to calculate the sum of digits of a number
        def sum_of_digits(num):
            return sum(int(digit) for digit in str(num))
        
        # Dictionary to store groups by sum of digits
        groups = defaultdict(int)
        
        # Fill the groups
        for i in range(1, n + 1):
            digit_sum = sum_of_digits(i)
            groups[digit_sum] += 1
        
        # Find the maximum group size
        max_size = max(groups.values())
        
        # Count how many groups have the largest size
        largest_group_count = sum(1 for size in groups.values() if size == max_size)
        
        return largest_group_count
