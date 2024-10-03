class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Initialize counters
        balance = 0
        needed_open = 0
        
        # Traverse the string
        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            
            # If balance goes negative, we need more opening brackets
            if balance < 0:
                needed_open += 1
                balance = 0
        
        # Return the sum of needed openings and remaining balance
        return needed_open + balance
