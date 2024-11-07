from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Dictionary to store the count of each domino in its canonical form
        domino_count = defaultdict(int)
        count = 0
        
        for domino in dominoes:
            # Sort the domino to ensure canonical form (min, max)
            key = tuple(sorted(domino))
            
            # If we've seen this domino before, add the number of pairs we can form
            count += domino_count[key]
            
            # Increment the count for this domino in its canonical form
            domino_count[key] += 1
        
        return count
