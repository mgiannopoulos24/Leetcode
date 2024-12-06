class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # Convert column letter to a number (1 for 'a', 2 for 'b', ..., 8 for 'h')
        col = ord(coordinates[0]) - ord('a') + 1
        # Convert row character to an integer
        row = int(coordinates[1])
        
        # Check if the sum of col and row is odd (white) or even (black)
        return (col + row) % 2 == 1
