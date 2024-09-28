from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        from collections import deque

        # Edge case: already at the target
        if target == 0:
            return 0

        # Initialize BFS
        queue = deque()
        queue.append((0, 1))  # (position, speed)
        visited = set()
        visited.add((0, 1))
        steps = 0

        while queue:
            # Process all states at the current level
            for _ in range(len(queue)):
                position, speed = queue.popleft()

                # Check if we've reached the target
                if position == target:
                    return steps

                # Instruction 'A' (Accelerate)
                new_position = position + speed
                new_speed = speed * 2
                state_A = (new_position, new_speed)
                # Only consider states within reasonable boundaries
                if 0 <= new_position <= 2 * target and state_A not in visited:
                    visited.add(state_A)
                    queue.append(state_A)

                # Instruction 'R' (Reverse)
                # Reverse only if the last action was not a reverse to avoid infinite loops
                # (This is optional but can speed up the BFS)
                new_speed_R = -1 if speed > 0 else 1
                state_R = (position, new_speed_R)
                if state_R not in visited:
                    visited.add(state_R)
                    queue.append(state_R)

            # Increment the number of steps after processing the current level
            steps += 1

        # If the target is not reachable (shouldn't happen with given constraints)
        return -1
