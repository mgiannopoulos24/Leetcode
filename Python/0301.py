from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string: str) -> bool:
            """Check if the string has valid parentheses."""
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        
        def generate_next_states(string: str) -> List[str]:
            """Generate all possible strings by removing one parenthesis."""
            next_states = []
            for i in range(len(string)):
                if string[i] not in ('(', ')'):
                    continue
                next_state = string[:i] + string[i+1:]
                if next_state not in visited:
                    next_states.append(next_state)
                    visited.add(next_state)
            return next_states
        
        # Initial check
        if is_valid(s):
            return [s]
        
        # BFS initialization
        visited = set([s])
        queue = deque([s])
        result = []
        found = False
        
        while queue:
            current_level_size = len(queue)
            level_results = []
            
            for _ in range(current_level_size):
                current = queue.popleft()
                
                if is_valid(current):
                    result.append(current)
                    found = True
                
                if found:
                    continue  # No need to generate more states for this level
                
                next_states = generate_next_states(current)
                queue.extend(next_states)
            
            if found:
                break
        
        return result
