class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # Initialize variables
        total_combinations = k ** n
        visited = set()
        result = ["0"] * n  # Start with "000...0" of length n
        start = "".join(result)
        
        visited.add(start)
        
        # Helper function for DFS
        def dfs(node):
            if len(visited) == total_combinations:
                return True
            
            last_digits = node[-(n - 1):] if n > 1 else ""  # n - 1 last digits
            
            for digit in range(k):
                next_node = last_digits + str(digit)
                if next_node not in visited:
                    visited.add(next_node)
                    result.append(str(digit))
                    if dfs(next_node):
                        return True
                    # Backtrack
                    visited.remove(next_node)
                    result.pop()
            
            return False
        
        # Start DFS from the initial node
        dfs(start)
        
        return "".join(result)
