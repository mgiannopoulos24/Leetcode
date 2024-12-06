from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        # Left-to-right pass
        operations = 0
        balls = 0
        for i in range(n):
            answer[i] += operations
            balls += int(boxes[i])  # Count of balls so far
            operations += balls     # Add balls to operations for the next position
        
        # Right-to-left pass
        operations = 0
        balls = 0
        for i in range(n - 1, -1, -1):
            answer[i] += operations
            balls += int(boxes[i])  # Count of balls so far
            operations += balls     # Add balls to operations for the previous position
        
        return answer
