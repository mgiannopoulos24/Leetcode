import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        total_tests = minutesToTest // minutesToDie + 1
        
        pigs = 0
        while (total_tests ** pigs) < buckets:
            pigs += 1
        
        return pigs
