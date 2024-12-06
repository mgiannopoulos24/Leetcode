class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # Create a dictionary to store the pairing for quick lookup
        pair_map = {}
        for x, y in pairs:
            pair_map[x] = y
            pair_map[y] = x
        
        # Create a ranking dictionary to determine the preference index of each friend for each person
        rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                rank[i][preferences[i][j]] = j
        
        unhappy_count = 0
        
        # Check each person to see if they are unhappy
        for x in range(n):
            y = pair_map[x]  # x is paired with y
            # Check if x is unhappy by comparing with the people x prefers over y
            for u in preferences[x][:rank[x][y]]:  # Check only friends u that are preferred over y
                v = pair_map[u]  # u is paired with v
                # Check if u also prefers x over v
                if rank[u][x] < rank[u][v]:
                    unhappy_count += 1
                    break
        
        return unhappy_count
