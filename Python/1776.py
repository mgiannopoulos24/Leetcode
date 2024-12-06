from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        answer = [-1.0] * n
        stack = []  # To keep track of cars for collision checking in reverse order

        # Traverse cars from the end to the start
        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]
            
            # Remove cars from the stack that cannot be collided with
            while stack:
                pos_next, speed_next, time_to_collide = stack[-1]
                
                # If the current car is slower or has the same speed as the car in front,
                # or if it cannot collide with the car on top of the stack before the next collision,
                # then pop it
                if speed <= speed_next or (time_to_collide > 0 and (pos_next - pos) / (speed - speed_next) > time_to_collide):
                    stack.pop()
                else:
                    break
            
            # Calculate the collision time if there is a car in the stack
            if stack:
                pos_next, speed_next, time_to_collide = stack[-1]
                answer[i] = (pos_next - pos) / (speed - speed_next)
            
            # Push the current car with its collision time onto the stack
            stack.append((pos, speed, answer[i]))

        return answer
