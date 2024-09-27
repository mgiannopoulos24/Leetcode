from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            # Process collisions
            while stack and asteroid < 0 and stack[-1] > 0:
                top = stack[-1]
                if top < -asteroid:
                    # The asteroid in the stack is smaller and will be destroyed
                    stack.pop()
                elif top == -asteroid:
                    # Both asteroids are the same size and will be destroyed
                    stack.pop()
                    break
                else:
                    # The asteroid in the stack is larger and the new asteroid is destroyed
                    break
            else:
                # If no collision or asteroid moving right, add it to the stack
                stack.append(asteroid)
        
        return stack
