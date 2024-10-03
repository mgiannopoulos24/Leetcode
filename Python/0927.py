from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total_ones = arr.count(1)
        
        # If there are no '1's, any partition will work
        if total_ones == 0:
            return [0, 2]  # Split after first and second elements
        
        # Total number of '1's must be divisible by 3
        if total_ones % 3 != 0:
            return [-1, -1]
        
        target_ones = total_ones // 3
        first = second = third = -1
        count = 0
        
        # Identify the starting index of the first '1' in each part
        for i, bit in enumerate(arr):
            if bit == 1:
                count += 1
                if count == 1:
                    first = i
                elif count == target_ones + 1:
                    second = i
                elif count == 2 * target_ones + 1:
                    third = i
        
        # Extract the pattern from the third part
        pattern = arr[third:]
        
        # Function to check if the pattern matches starting from a given index
        def check(start):
            for i in range(len(pattern)):
                if start + i >= len(arr) or arr[start + i] != pattern[i]:
                    return False
            return True
        
        # Verify the pattern in the first and second parts
        if not check(first) or not check(second):
            return [-1, -1]
        
        # Determine the end indices of the first and second parts
        i = first + len(pattern) - 1
        j = second + len(pattern)
        
        return [i, j]
