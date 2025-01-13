from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count0 = count1 = count2 = 0
        for stone in stones:
            if stone % 3 == 0:
                count0 += 1
            elif stone % 3 == 1:
                count1 += 1
            else:
                count2 += 1
        
        if count0 % 2 == 0:
            return count1 >= 1 and count2 >= 1
        else:
            return abs(count1 - count2) > 2