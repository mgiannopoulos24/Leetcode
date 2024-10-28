class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Step 1: Count the frequency of each character in the string
        char_count = {c: 0 for c in s}
        for c in s:
            char_count[c] += 1
        
        # Stack to store the result characters
        stack = []
        
        # Set to track visited characters (i.e., already in the stack)
        visited = set()
        
        # Step 2: Iterate over the string
        for c in s:
            # Decrease the frequency count for this character
            char_count[c] -= 1
            
            # If the character is already in the stack, skip it
            if c in visited:
                continue
            
            # Step 3: Maintain the lexicographically smallest order
            # If the current character is smaller than the last character in the stack
            # and the last character appears later, pop the stack
            while stack and c < stack[-1] and char_count[stack[-1]] > 0:
                removed = stack.pop()
                visited.remove(removed)  # Mark it as not visited, since it's being removed
            
            # Add the current character to the stack and mark it as visited
            stack.append(c)
            visited.add(c)
        
        # Step 4: Join the stack to form the result string
        return ''.join(stack)
