from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Record the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        # Result list to store the sizes of partitions
        result = []
        
        # Pointers to track the start and end of the current partition
        start, end = 0, 0
        
        # Step 2: Iterate through the string to find partitions
        for i, char in enumerate(s):
            # Extend the end of the current partition
            end = max(end, last_occurrence[char])
            
            # If the current index matches the end, we found a partition
            if i == end:
                # The size of the partition
                result.append(end - start + 1)
                # Move start to the next index after the current partition
                start = i + 1
        
        return result
