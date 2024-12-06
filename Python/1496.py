class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Start at the origin
        x, y = 0, 0
        visited = set()
        visited.add((x, y))  # Add the starting point
        
        # Traverse the path
        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
            
            # Check if the current position is already visited
            if (x, y) in visited:
                return True
            visited.add((x, y))
        
        # No crossing found
        return False
