from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        queue = deque([start])
        
        while queue:
            i = queue.popleft()
            if arr[i] == 0:
                return True
            if visited[i]:
                continue
            visited[i] = True
            
            # Check if we can move left and right within the bounds of the array
            if i + arr[i] < n:
                queue.append(i + arr[i])
            if i - arr[i] >= 0:
                queue.append(i - arr[i])
        
        return False
