class Solution:
    def reformat(self, s: str) -> str:
        # Separate letters and digits into two lists
        letters = []
        digits = []
        
        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)
        
        # If the absolute difference in counts is more than 1, return ""
        if abs(len(letters) - len(digits)) > 1:
            return ""
        
        # Decide whether to start with a letter or a digit based on their counts
        if len(digits) > len(letters):
            result = []
            while digits or letters:
                if digits:
                    result.append(digits.pop(0))
                if letters:
                    result.append(letters.pop(0))
        else:
            result = []
            while letters or digits:
                if letters:
                    result.append(letters.pop(0))
                if digits:
                    result.append(digits.pop(0))
        
        return "".join(result)