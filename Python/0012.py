class Solution:
    def intToRoman(self, num: int) -> str:
        # Define Roman numeral symbols and their corresponding values
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        # Initialize an empty string to store the Roman numeral representation
        result = ''
        
        # Initialize index to iterate through symbols and values
        i = 0
        
        # Iterate through each symbol and value pair
        while num > 0:
            # While num is greater than or equal to the current value, append the corresponding symbol
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]  # Subtract the value from num to reduce it
            i += 1  # Move to the next symbol
        
        return result  # Return the final Roman numeral representation
