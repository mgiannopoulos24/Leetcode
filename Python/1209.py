class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Stack to store pairs of (character, count)
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                # If the current char is the same as the last one in the stack, increment its count
                stack[-1] = (char, stack[-1][1] + 1)
                
                # If the count reaches k, remove it from the stack
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # Otherwise, push a new character with count 1
                stack.append((char, 1))
        
        # Rebuild the final string from the stack
        result = []
        for char, count in stack:
            result.append(char * count)
        
        return ''.join(result)
