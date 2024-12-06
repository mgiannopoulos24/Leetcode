class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(curr):
            # If the current string is of length n, add it to the result
            if len(curr) == n:
                result.append(curr)
                return
            
            # Try adding 'a', 'b', 'c' to the current string
            for char in ['a', 'b', 'c']:
                if not curr or curr[-1] != char:
                    backtrack(curr + char)
        
        result = []
        backtrack("")  # Start backtracking with an empty string
        
        # Check if we have at least k happy strings
        if len(result) < k:
            return ""
        return result[k - 1]  # Return the k-th happy string (1-indexed)