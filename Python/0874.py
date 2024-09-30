from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Define direction vectors for North, East, South, and West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initial position and direction (facing North, index 0)
        x, y = 0, 0
        direction_index = 0
        
        # Convert obstacles to a set for fast lookup
        obstacle_set = set(tuple(obs) for obs in obstacles)
        
        # Initialize maximum distance squared
        max_distance_squared = 0
        
        # Process each command
        for command in commands:
            if command == -2:
                # Turn left
                direction_index = (direction_index - 1) % 4
            elif command == -1:
                # Turn right
                direction_index = (direction_index + 1) % 4
            else:
                # Move forward
                dx, dy = directions[direction_index]
                for _ in range(command):
                    # Move one step in the current direction
                    x += dx
                    y += dy
                    # Check if the new position hits an obstacle
                    if (x, y) in obstacle_set:
                        x -= dx
                        y -= dy
                        break
                    # Update the maximum distance squared
                    max_distance_squared = max(max_distance_squared, x * x + y * y)
        
        return max_distance_squared
