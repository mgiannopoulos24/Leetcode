import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Define the regex pattern for a valid number
        pattern = re.compile(r'''
            ^                    # Start of the string
            [+-]?                # Optional sign
            (                    # Start of number part
                (                # Start of integer part
                    \d+          # One or more digits
                    (\.\d*)?     # Optional dot followed by zero or more digits
                |                # or
                    \.\d+        # A dot followed by one or more digits
                )                # End of integer part
                (                # Optional exponent part
                    (e|E)        # Exponent part
                    [+-]?        # Optional sign for exponent
                    \d+          # One or more digits
                )?               # Exponent part is optional
            )                    # End of number part
            $                    # End of the string
        ''', re.VERBOSE)
        
        return bool(pattern.match(s))
