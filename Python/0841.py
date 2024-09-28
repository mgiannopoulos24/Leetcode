from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        num_visited = 0
        
        while queue:
            room = queue.popleft()
            num_visited += 1
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    queue.append(key)
        
        return num_visited == n
