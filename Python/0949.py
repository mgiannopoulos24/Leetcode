from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = -1  # Initialize max_time to -1, meaning no valid time found yet
        
        # Generate all permutations of the array
        for perm in permutations(arr):
            # Convert permutation to "HHMM" format
            hours = perm[0] * 10 + perm[1]
            minutes = perm[2] * 10 + perm[3]
            
            # Check if the time is valid
            if 0 <= hours < 24 and 0 <= minutes < 60:
                # Update the maximum valid time found
                total_minutes = hours * 60 + minutes
                if total_minutes > max_time:
                    max_time = total_minutes
        
        if max_time == -1:
            return ""  # No valid time found
        
        # Convert max_time back to "HH:MM" format
        hours = max_time // 60
        minutes = max_time % 60
        return f"{hours:02}:{minutes:02}"
