class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # Split the text into words
        words = text.split()
        result = []
        
        # Iterate through the words, but stop before the last two words
        for i in range(len(words) - 2):
            # Check if the current and next word match 'first' and 'second'
            if words[i] == first and words[i + 1] == second:
                # Add the third word to the result list
                result.append(words[i + 2])
        
        return result
