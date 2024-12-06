class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        
        # Loop through possible starting digits
        for start in range(1, 10):
            num = start
            next_digit = start
            
            # Build the sequential number
            while num <= high and next_digit < 9:
                next_digit += 1
                num = num * 10 + next_digit  # Append the next sequential digit
                
                # If num is within the range [low, high], add to the result
                if low <= num <= high:
                    result.append(num)
        
        # Return the sorted list of sequential digits
        return sorted(result)
