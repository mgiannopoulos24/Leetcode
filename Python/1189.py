from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Step 1: Count frequencies of each character in the input text
        char_count = Counter(text)
        
        # Step 2: Define the character frequency needed for "balloon"
        balloon_count = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }
        
        # Step 3: Determine the maximum number of "balloon" instances
        # by finding the minimum ratio of available characters to required characters
        max_balloons = float('inf')
        for char, count in balloon_count.items():
            max_balloons = min(max_balloons, char_count[char] // count)
        
        return max_balloons
