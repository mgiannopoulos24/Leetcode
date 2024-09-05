from math import gcd
from functools import reduce

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Helper function to calculate least common multiple
        def lcm(a, b):
            return abs(a * b) // gcd(a, b)
        
        # Helper function to parse the expression and extract fractions
        def parse_expression(expression):
            fractions = []
            index = 0
            while index < len(expression):
                if expression[index] in '+-':
                    sign = 1 if expression[index] == '+' else -1
                    index += 1
                else:
                    sign = 1
                
                num_start = index
                while index < len(expression) and expression[index] != '/':
                    index += 1
                numerator = int(expression[num_start:index]) * sign
                
                index += 1  # Skip the '/'
                
                denom_start = index
                while index < len(expression) and expression[index].isdigit():
                    index += 1
                denominator = int(expression[denom_start:index])
                
                fractions.append((numerator, denominator))
            
            return fractions
        
        # Parse the fractions from the expression
        fractions = parse_expression(expression)
        
        # Find the least common denominator (LCD) for all fractions
        denominators = [denom for _, denom in fractions]
        lcd = reduce(lcm, denominators)
        
        # Convert all fractions to the common denominator and sum them up
        numerator_sum = 0
        for numerator, denominator in fractions:
            numerator_sum += numerator * (lcd // denominator)
        
        # Simplify the result by using GCD
        common_divisor = gcd(abs(numerator_sum), lcd)
        numerator_sum //= common_divisor
        lcd //= common_divisor
        
        # Format the result as a fraction
        return f"{numerator_sum}/{lcd}"
