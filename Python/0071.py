class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by '/'
        components = path.split('/')
        
        # Initialize an empty stack to build the canonical path
        stack = []
        
        for part in components:
            if part == '..':
                # Pop from the stack if ".." and the stack is not empty
                if stack:
                    stack.pop()
            elif part and part != '.':
                # Add valid directory names to the stack
                stack.append(part)
        
        # Join the stack to form the simplified path
        simplified_path = '/' + '/'.join(stack)
        
        return simplified_path
