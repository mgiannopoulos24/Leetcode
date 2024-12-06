class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        # List of tuples (count, char)
        count = [('a', a), ('b', b), ('c', c)]
        
        while True:
            # Sort the list by count in descending order
            count.sort(key=lambda x: -x[1])
            
            # Try to add the most frequent character
            added = False
            for i in range(3):
                char, char_count = count[i]
                # If this character can be added (it's not the same as the last two)
                if char_count > 0 and not (len(result) >= 2 and result[-1] == result[-2] == char):
                    result.append(char)
                    count[i] = (char, char_count - 1)  # Decrease the count
                    added = True
                    break
            
            # If no character was added, stop the process
            if not added:
                break
        
        return ''.join(result)