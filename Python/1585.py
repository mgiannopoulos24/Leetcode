from collections import deque

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        # Create deques for each digit (0-9) to store their indices in s
        index_deques = [deque() for _ in range(10)]
        
        # Populate the deques with the indices of each digit in s
        for i, char in enumerate(s):
            index_deques[int(char)].append(i)
        
        # Now process each character in t
        for char in t:
            digit = int(char)
            
            # If there's no occurrence of digit in s that can match the current t digit, return False
            if not index_deques[digit]:
                return False
            
            # Get the index of the current digit from s that we want to match
            current_index = index_deques[digit].popleft()
            
            # Ensure that there are no smaller digits that appear before current_index in s,
            # since sorting would require those to be resolved first
            for smaller_digit in range(digit):
                if index_deques[smaller_digit] and index_deques[smaller_digit][0] < current_index:
                    return False
        
        # If we successfully match all characters, return True
        return True
