MOD = 10**9 + 7

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        
        # Step 1: Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        
        # Calculate all factorials % MOD
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        # Calculate inverse factorials % MOD using Fermat's little theorem
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        
        # Step 2: Build the graph (tree structure)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[prevRoom[i]].append(i)
        
        # Step 3: DFS to calculate dp[i] for each room i
        dp = [0] * n
        size = [0] * n  # size[i] is the number of nodes in the subtree rooted at i
        
        def dfs(node):
            dp[node] = 1  # Base case: the subtree of a leaf room has 1 way to build (itself)
            size[node] = 1  # A room by itself counts as one room
            total_size = 0  # Accumulating size of all children
            
            for child in children[node]:
                dfs(child)
                # Multiply dp[node] with dp[child] and the number of ways to interleave the children
                dp[node] = dp[node] * dp[child] % MOD
                # The number of ways to interleave child subtrees is C(total_size + size[child], size[child])
                dp[node] = dp[node] * fact[total_size + size[child]] * inv_fact[total_size] % MOD * inv_fact[size[child]] % MOD
                total_size += size[child]
            
            # Add the size of the current node itself
            size[node] += total_size
        
        # Start DFS from node 0
        dfs(0)
        
        # The final answer is stored in dp[0] as it represents the number of ways to build the entire structure
        return dp[0]

