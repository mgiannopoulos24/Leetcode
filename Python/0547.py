from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        
        def dfs(city: int):
            stack = [city]
            while stack:
                node = stack.pop()
                for neighbor in range(n):
                    if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
        
        num_provinces = 0
        
        for i in range(n):
            if not visited[i]:
                # Start a new DFS from this city
                visited[i] = True
                dfs(i)
                num_provinces += 1
        
        return num_provinces
