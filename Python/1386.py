from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Dictionary to store reserved seats for each row
        reserved_map = defaultdict(set)
        
        # Populate the reserved seats for each row
        for row, seat in reservedSeats:
            reserved_map[row].add(seat)
        
        # Maximum number of groups we can place without considering reserved seats
        max_groups = (n - len(reserved_map)) * 2
        
        # Process rows that have reserved seats
        for row, reserved in reserved_map.items():
            left_block = all(seat not in reserved for seat in [2, 3, 4, 5])
            middle_block = all(seat not in reserved for seat in [4, 5, 6, 7])
            right_block = all(seat not in reserved for seat in [6, 7, 8, 9])
            
            # Check how many groups can fit in this row
            if left_block and right_block:
                max_groups += 2  # Both left and right blocks are available
            elif left_block or right_block or middle_block:
                max_groups += 1  # Only one block is available
            
        return max_groups
