class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # Split the sentence into tokens
        tokens = s.split()
        
        # Extract numbers from the tokens
        numbers = []
        for token in tokens:
            if token.isdigit():
                numbers.append(int(token))
        
        # Check if the numbers are strictly increasing
        for i in range(1, len(numbers)):
            if numbers[i] <= numbers[i-1]:
                return False
        
        return True