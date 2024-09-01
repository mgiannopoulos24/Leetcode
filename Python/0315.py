from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Step 1: Coordinate compression
        sorted_nums = sorted(set(nums))  # Get unique elements sorted
        ranks = {num: i + 1 for i, num in enumerate(sorted_nums)}  # Map each number to its rank
        
        # Step 2: Initialize a BIT
        def update(bit, index, value):
            while index < len(bit):
                bit[index] += value
                index += index & -index

        def query(bit, index):
            sum = 0
            while index > 0:
                sum += bit[index]
                index -= index & -index
            return sum

        # Step 3: Process numbers from right to left
        bit = [0] * (len(ranks) + 1)  # BIT size is based on the unique ranks
        result = []
        for num in reversed(nums):
            rank = ranks[num]
            result.append(query(bit, rank - 1))  # Get count of smaller elements to the right
            update(bit, rank, 1)  # Add this element to the BIT
        
        return result[::-1]  # Reverse result since we processed from right to left
