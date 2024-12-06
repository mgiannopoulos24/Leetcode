from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Step 1: Count the frequency of each element
        freq = Counter(arr)
        
        # Step 2: Sort the frequencies in increasing order
        freq_values = sorted(freq.values())
        
        # Step 3: Remove elements with the smallest frequencies first
        remaining_unique = len(freq_values)  # Initial number of unique elements
        for f in freq_values:
            if k >= f:
                k -= f
                remaining_unique -= 1  # We completely remove this unique element
            else:
                break  # We can't remove this entire group
        
        # Step 4: Return the number of remaining unique elements
        return remaining_unique
