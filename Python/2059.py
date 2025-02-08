from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        queue = deque()
        queue.append((start, 0))  # (current value, number of operations)
        visited = set()
        visited.add(start)
        
        while queue:
            current, steps = queue.popleft()
            
            for num in nums:
                # Perform addition
                new_value = current + num
                if new_value == goal:
                    return steps + 1
                if 0 <= new_value <= 1000 and new_value not in visited:
                    visited.add(new_value)
                    queue.append((new_value, steps + 1))
                
                # Perform subtraction
                new_value = current - num
                if new_value == goal:
                    return steps + 1
                if 0 <= new_value <= 1000 and new_value not in visited:
                    visited.add(new_value)
                    queue.append((new_value, steps + 1))
                
                # Perform XOR
                new_value = current ^ num
                if new_value == goal:
                    return steps + 1
                if 0 <= new_value <= 1000 and new_value not in visited:
                    visited.add(new_value)
                    queue.append((new_value, steps + 1))
        
        return -1