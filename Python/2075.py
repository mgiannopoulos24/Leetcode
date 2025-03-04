class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        # Calculate the number of columns
        length = len(encodedText)
        cols = length // rows
        
        # Initialize the matrix
        matrix = [[' ' for _ in range(cols)] for _ in range(rows)]
        
        # Fill the matrix row-wise with encodedText
        index = 0
        for row in range(rows):
            for col in range(cols):
                if index < length:
                    matrix[row][col] = encodedText[index]
                    index += 1
                else:
                    break
        
        # Extract the originalText by reading diagonally
        originalText = []
        for diagonal in range(cols):
            row = 0
            col = diagonal
            while row < rows and col < cols:
                originalText.append(matrix[row][col])
                row += 1
                col += 1
        
        # Remove trailing spaces
        return ''.join(originalText).rstrip()