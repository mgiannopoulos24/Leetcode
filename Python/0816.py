from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def generate_valid_numbers(part: str) -> List[str]:
            n = len(part)
            valid_numbers = []
            
            # If the part is a valid integer
            if n == 1 or (part[0] != '0'):  # Valid integer with no leading zero
                valid_numbers.append(part)
            
            # Generate decimals, if possible
            for i in range(1, n):
                left, right = part[:i], part[i:]
                if (left == "0" or left[0] != '0') and right[-1] != '0':  # Valid decimal form
                    valid_numbers.append(left + '.' + right)
                    
            return valid_numbers

        # Remove the parentheses from the input string
        s = s[1:-1]
        n = len(s)
        result = []
        
        # Try every possible split point between x and y
        for i in range(1, n):
            x_part = s[:i]
            y_part = s[i:]
            
            x_candidates = generate_valid_numbers(x_part)
            y_candidates = generate_valid_numbers(y_part)
            
            # Combine all valid x and y pairs
            for x in x_candidates:
                for y in y_candidates:
                    result.append(f"({x}, {y})")
        
        return result
