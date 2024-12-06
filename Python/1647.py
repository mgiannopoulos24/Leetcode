from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        # Step 1: Count the frequency of each character
        freq = Counter(s)
        
        # Step 2: Use a set to track used frequencies
        used_frequencies = set()
        deletions = 0
        
        # Step 3: Iterate over character frequencies
        for char, count in freq.items():
            # Reduce the frequency until it is unique
            while count > 0 and count in used_frequencies:
                count -= 1
                deletions += 1
            # Add the final frequency to the set of used frequencies
            if count > 0:
                used_frequencies.add(count)
        
        return deletions
