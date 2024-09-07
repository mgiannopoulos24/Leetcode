import re

class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse_side(side):
            # Initialize coefficients and constants
            x_coeff = 0
            constant = 0
            
            # Find all terms using regular expression
            terms = re.findall(r'[+-]?\d*x?', side)
            
            for term in terms:
                if not term:
                    continue
                if 'x' in term:
                    # Remove 'x' and handle coefficient
                    coeff = term.replace('x', '')
                    if coeff == '' or coeff == '+':
                        x_coeff += 1
                    elif coeff == '-':
                        x_coeff -= 1
                    else:
                        x_coeff += int(coeff)
                else:
                    # Handle constant term
                    if term:
                        constant += int(term)
                        
            return x_coeff, constant
        
        # Split the equation into left and right sides
        left, right = equation.split('=')
        
        # Parse both sides
        left_x_coeff, left_const = parse_side(left)
        right_x_coeff, right_const = parse_side(right)
        
        # Combine terms
        x_coeff = left_x_coeff - right_x_coeff
        constant = right_const - left_const
        
        # Determine the result
        if x_coeff == 0:
            if constant == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return f"x={constant // x_coeff}"