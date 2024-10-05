from typing import List
from collections import deque

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        
        # Use a queue for BFS
        queue = deque([i for i in range(1, 10)])  # Start with digits 1 to 9
        
        while queue:
            num = queue.popleft()
            # If the number has reached the desired length, add it to the result
            if len(str(num)) == n:
                result.append(num)
            else:
                # Get the last digit of the current number
                last_digit = num % 10
                
                # Compute the next possible digits
                next_digits = set()
                if last_digit + k < 10:
                    next_digits.add(last_digit + k)
                if last_digit - k >= 0 and k != 0:
                    next_digits.add(last_digit - k)
                
                # Append each valid digit to the current number and add to the queue
                for digit in next_digits:
                    new_num = num * 10 + digit
                    queue.append(new_num)
        
        return result
