from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Initialize a set to store sequences we've seen and another for repeated sequences
        seen = set()
        repeated = set()
        
        # Iterate through the string, considering each 10-letter-long substring
        for i in range(len(s) - 9):
            # Extract the current 10-letter-long substring
            sequence = s[i:i + 10]
            
            # If the sequence is already in the seen set, add it to the repeated set
            if sequence in seen:
                repeated.add(sequence)
            else:
                # Otherwise, add it to the seen set
                seen.add(sequence)
        
        # Convert the set of repeated sequences to a list and return
        return list(repeated)
