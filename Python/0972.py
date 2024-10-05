from fractions import Fraction

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def to_rational(number: str) -> Fraction:
            if '(' in number:
                # Split the number into non-repeating and repeating part
                non_repeat, repeat = number.split('(')
                repeat = repeat.rstrip(')')
            else:
                non_repeat, repeat = number, ''
            
            if '.' in non_repeat:
                integer_part, non_repeat = non_repeat.split('.')
            else:
                integer_part, non_repeat = non_repeat, ''
            
            # Convert integer part
            if integer_part:
                result = Fraction(int(integer_part))
            else:
                result = Fraction(0)
            
            # Add non-repeating decimal part
            if non_repeat:
                result += Fraction(int(non_repeat), 10 ** len(non_repeat))
            
            # Add repeating decimal part, if it exists
            if repeat:
                # Length of repeating part
                len_repeat = len(repeat)
                repeat_value = int(repeat)
                denominator = (10 ** len_repeat - 1) * (10 ** len(non_repeat))
                repeating_fraction = Fraction(repeat_value, denominator)
                result += repeating_fraction
            
            return result
        
        return to_rational(s) == to_rational(t)
