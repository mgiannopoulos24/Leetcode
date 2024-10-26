class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # Step 1: Create an adjacency list to represent the graph
        graph = [[] for _ in range(n)]
        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)
        
        # Step 2: Initialize the result array with zeros (no flowers assigned yet)
        answer = [0] * n
        
        # Step 3: Assign flower types to each garden
        for i in range(n):
            # Find the flower types of neighbors
            used_flowers = {answer[neighbor] for neighbor in graph[i] if answer[neighbor] != 0}
            
            # Assign the smallest flower type that is not used by the neighbors
            for flower in range(1, 5):
                if flower not in used_flowers:
                    answer[i] = flower
                    break
        
        return answer
