class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Split the input by lines
        lines = input.split('\n')
        
        # Stack to keep track of the path lengths at each level
        stack = []
        max_length = 0
        
        for line in lines:
            # Determine the current depth by counting the number of tabs
            depth = line.count('\t')
            # Get the name of the file or directory (removing tabs)
            name = line.lstrip('\t')
            
            # Adjust stack to the current depth
            while len(stack) > depth:
                stack.pop()
            
            # Calculate the current length (adding the length of the name and a slash if not at root)
            current_length = (stack[-1] if stack else 0) + len(name) + 1  # +1 for the '/' or starting position
            
            # Check if it's a file (contains a dot)
            if '.' in name:
                # Update the maximum length found
                max_length = max(max_length, current_length - 1)  # Remove the trailing '/'
            else:
                # It's a directory; add the length to the stack
                stack.append(current_length)
        
        return max_length
