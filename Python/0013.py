class Solution:
    def romanToInt(self, s: str) -> int:
        # Check if the input string is empty
        if not s:
            return 0
        
        # Dictionary to store the integer values of Roman numerals
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # Initialize the total sum
        total = 0
        # Length of the input string
        n = len(s)
        
        # Iterate through the string
        for i in range(n):
            # If current character value is less than next character value, subtract current value from total
            if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                # Otherwise, add current character value to total
                total += roman_to_int[s[i]]
        
        # Return the total sum
        return total
