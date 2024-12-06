from typing import List
from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden_set = set(forbidden)
        max_limit = max([x] + forbidden) + a + b + 2000  # Define an upper limit for positions

        queue = deque()
        queue.append((0, False, 0))  # position, last_was_backward, steps
        visited = set()
        visited.add((0, False))

        while queue:
            pos, last_was_backward, steps = queue.popleft()

            # If we've reached the target position, return the steps taken
            if pos == x:
                return steps

            # Jump forward
            next_forward = pos + a
            if (next_forward <= max_limit and next_forward not in forbidden_set
                and (next_forward, False) not in visited):
                visited.add((next_forward, False))
                queue.append((next_forward, False, steps + 1))

            # Jump backward (only if the last jump was not backward)
            if not last_was_backward:
                next_backward = pos - b
                if (next_backward >= 0 and next_backward not in forbidden_set
                    and (next_backward, True) not in visited):
                    visited.add((next_backward, True))
                    queue.append((next_backward, True, steps + 1))

        # If the queue is empty and we haven't reached x, return -1
        return -1
