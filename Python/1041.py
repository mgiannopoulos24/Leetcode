class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Directions: 0 -> North, 1 -> East, 2 -> South, 3 -> West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initial position and direction
        x, y = 0, 0  # Starting at (0, 0)
        direction = 0  # Initially facing north (index 0 in directions)
        
        # Process each instruction
        for instruction in instructions:
            if instruction == 'G':  # Go straight
                dx, dy = directions[direction]
                x += dx
                y += dy
            elif instruction == 'L':  # Turn left
                direction = (direction - 1) % 4
            elif instruction == 'R':  # Turn right
                direction = (direction + 1) % 4
        
        # After processing the instructions:
        # - If we're back at (0, 0), it's bounded.
        # - If we're not facing north, the robot will be bounded in a cycle.
        return (x == 0 and y == 0) or direction != 0
