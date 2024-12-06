class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Initialize degree array and connection set
        degree = [0] * n
        connected = set()
        
        # Step 2: Build the degree array and connection set
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            connected.add((a, b))
            connected.add((b, a))  # To account for bidirectional roads
        
        # Step 3: Calculate the maximal network rank
        max_rank = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the network rank for cities i and j
                rank = degree[i] + degree[j]
                if (i, j) in connected:  # If they are directly connected, subtract 1
                    rank -= 1
                max_rank = max(max_rank, rank)
        
        return max_rank
