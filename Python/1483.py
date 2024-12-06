class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        # Maximum power of 2 we need to consider (log2(n))
        max_power = 0
        while (1 << max_power) <= n:
            max_power += 1
        
        # DP table: dp[node][j] stores the 2^j-th ancestor of node
        self.dp = [[-1] * max_power for _ in range(n)]
        
        # Initialize the first ancestor (2^0 = 1-step ancestor, i.e., parent)
        for i in range(n):
            self.dp[i][0] = parent[i]
        
        # Fill the DP table
        for j in range(1, max_power):
            for i in range(n):
                if self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
    
    def getKthAncestor(self, node: int, k: int) -> int:
        # Jump upwards using the precomputed DP table
        max_power = len(self.dp[0])
        for j in range(max_power):
            if k & (1 << j):  # Check if the j-th bit is set in k
                node = self.dp[node][j]
                if node == -1:  # No such ancestor exists
                    return -1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)