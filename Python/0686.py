class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Calculate the minimum number of repetitions needed
        len_a = len(a)
        len_b = len(b)
        
        # Calculate minimum repeats
        min_repeats = -(-len_b // len_a)  # This is the ceiling of len_b / len_a
        
        # Check if b is a substring of the repeated string
        for i in range(2):  # Check the minimum and one more repeat
            repeated_a = a * (min_repeats + i)
            if b in repeated_a:
                return min_repeats + i
        
        return -1
