from typing import List
from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Count the frequency of each card
        freq = Counter(deck)
        
        # Extract the frequencies
        freq_values = list(freq.values())
        
        # Compute the GCD of all frequencies
        def find_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        overall_gcd = reduce(find_gcd, freq_values)
        
        # Check if the GCD is greater than 1
        return overall_gcd > 1
