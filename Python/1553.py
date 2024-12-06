from collections import deque

class Solution:
    def minDays(self, n: int) -> int:
        # BFS approach to avoid recursion limits
        queue = deque([(n, 0)])  # (current number of oranges, days taken)
        visited = set([n])  # To avoid revisiting the same state
        
        while queue:
            curr, days = queue.popleft()
            
            # If no oranges are left, return the number of days taken
            if curr == 0:
                return days
            
            # Explore the possible operations:
            # 1. Eat one orange
            if curr - 1 not in visited:
                visited.add(curr - 1)
                queue.append((curr - 1, days + 1))
            
            # 2. Eat n // 2 oranges if divisible by 2
            if curr % 2 == 0 and curr // 2 not in visited:
                visited.add(curr // 2)
                queue.append((curr // 2, days + 1))
            
            # 3. Eat 2 * (n // 3) oranges if divisible by 3
            if curr % 3 == 0 and curr // 3 not in visited:
                visited.add(curr // 3)
                queue.append((curr // 3, days + 1))
