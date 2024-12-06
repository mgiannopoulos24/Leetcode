class Solution:
    def secondHighest(self, s: str) -> int:
        # Step 1: Extract unique digits from the string
        unique_digits = set(int(char) for char in s if char.isdigit())
        
        # Step 2: Sort unique digits in descending order
        sorted_digits = sorted(unique_digits, reverse=True)
        
        # Step 3: Check if there is a second largest digit
        if len(sorted_digits) >= 2:
            return sorted_digits[1]  # Return the second largest
        else:
            return -1  # Return -1 if there's no second largest
