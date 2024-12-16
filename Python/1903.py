class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Iterate from the end of the string
        for i in range(len(num) - 1, -1, -1):
            # Check if the current digit is odd
            if int(num[i]) % 2 == 1:
                return num[:i + 1]  # Return the substring up to and including this digit
        return ""  # No odd number found
