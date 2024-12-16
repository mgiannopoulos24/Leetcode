class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)
        
        for char in s:
            # Add character to stack
            stack.append(char)
            
            # Check if the last `len(part)` characters match `part`
            if len(stack) >= part_len and ''.join(stack[-part_len:]) == part:
                # Remove the last `len(part)` characters
                del stack[-part_len:]
        
        # Reconstruct the string from the stack
        return ''.join(stack)
