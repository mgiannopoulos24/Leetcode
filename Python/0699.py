class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        intervals = []  # Will store intervals and heights [(left, right, height)]
        max_height = 0  # To track the global max height at any point
        result = []
        
        for left, size in positions:
            right = left + size  # Calculate the right boundary of the square
            current_max = 0  # Find the max height the current square can land on
            
            # Check for overlaps with existing intervals
            for l, r, h in intervals:
                if not (r <= left or l >= right):  # Check if there is an overlap
                    current_max = max(current_max, h)
            
            # The height of the current square is size + current_max
            new_height = current_max + size
            intervals.append((left, right, new_height))  # Add the new interval and height
            max_height = max(max_height, new_height)  # Update the global max height
            result.append(max_height)  # Store the current max height after this square
        
        return result
