from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # BFS to explore all possible transformations
        seen = set()  # To track visited strings
        queue = deque([s])  # Initialize BFS queue
        smallest = s  # To track the lexicographically smallest string
        
        while queue:
            current = queue.popleft()
            
            # Update smallest if current string is smaller
            if current < smallest:
                smallest = current
            
            # Apply the add operation to odd indices
            # Convert the string to list for easier manipulation
            chars = list(current)
            for i in range(1, len(chars), 2):  # Add 'a' to odd-indexed positions
                chars[i] = str((int(chars[i]) + a) % 10)
            add_op_result = ''.join(chars)
            
            # If we haven't seen this result, add it to the queue
            if add_op_result not in seen:
                seen.add(add_op_result)
                queue.append(add_op_result)
            
            # Apply the rotate operation
            rotate_op_result = current[-b:] + current[:-b]
            
            # If we haven't seen this result, add it to the queue
            if rotate_op_result not in seen:
                seen.add(rotate_op_result)
                queue.append(rotate_op_result)
        
        return smallest
