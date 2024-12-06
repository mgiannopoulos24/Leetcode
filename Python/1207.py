from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Step 1: Count the frequency of each number in the array
        freq = Counter(arr)
        
        # Step 2: Get the set of frequencies
        freq_values = list(freq.values())
        
        # Step 3: Check if all frequencies are unique by comparing with a set
        return len(freq_values) == len(set(freq_values))
