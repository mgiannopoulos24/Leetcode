class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # Sort digits in descending order to try to form the largest possible number
        digits.sort(reverse=True)
        
        # Compute the sum of the digits
        total_sum = sum(digits)
        
        # Helper function to remove a digit with a given remainder
        def remove_digit_with_remainder(digits, remainder):
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] % 3 == remainder:
                    return digits.pop(i)
            return False

        # Case when sum % 3 == 1, we need to remove a digit with remainder 1
        if total_sum % 3 == 1:
            if not remove_digit_with_remainder(digits, 1):
                # If no remainder 1 digit, remove two digits with remainder 2
                remove_digit_with_remainder(digits, 2)
                remove_digit_with_remainder(digits, 2)
        
        # Case when sum % 3 == 2, we need to remove a digit with remainder 2
        elif total_sum % 3 == 2:
            if not remove_digit_with_remainder(digits, 2):
                # If no remainder 2 digit, remove two digits with remainder 1
                remove_digit_with_remainder(digits, 1)
                remove_digit_with_remainder(digits, 1)
        
        # If after removal the list is empty, return an empty string
        if not digits:
            return ""
        
        # If the largest number is "0", then return "0" (handle leading zeros)
        if digits[0] == 0:
            return "0"
        
        # Join the digits into a string and return
        return ''.join(map(str, digits))
