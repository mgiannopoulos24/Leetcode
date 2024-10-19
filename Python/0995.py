from collections import deque
from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        flip_effect = 0
        flip_queue = deque()  # To keep track of flips affecting the current index
        
        for i in range(n):
            if flip_queue and flip_queue[0] <= i:
                flip_effect ^= 1
                flip_queue.popleft()
                
            if nums[i] == flip_effect:
                if i + k > n:
                    return -1
                flips += 1
                flip_effect ^= 1
                flip_queue.append(i + k)
        
        return flips
