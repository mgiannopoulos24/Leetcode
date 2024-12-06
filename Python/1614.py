class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0  # To keep track of the maximum depth
        current_depth = 0  # To keep track of the current depth
        
        for char in s:
            if char == '(':
                current_depth += 1  # Increase depth for open parenthesis
                max_depth = max(max_depth, current_depth)  # Update max depth
            elif char == ')':
                current_depth -= 1  # Decrease depth for close parenthesis
        
        return max_depth
