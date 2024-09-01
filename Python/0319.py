import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # The number of bulbs that remain on is equal to the count of perfect squares up to n
        return int(math.sqrt(n))
