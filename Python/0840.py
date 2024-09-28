class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(square):
            """ Check if a 3x3 list of lists is a magic square """
            magic_sum = 15
            for i in range(3):
                if sum(square[i]) != magic_sum:
                    return False
            for j in range(3):
                if sum(square[i][j] for i in range(3)) != magic_sum:
                    return False
            if sum(square[i][i] for i in range(3)) != magic_sum:
                return False
            if sum(square[i][2 - i] for i in range(3)) != magic_sum:
                return False
            return True
        
        # All possible 3x3 magic squares
        magic_squares = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
        ]
        
        def extractSubgrid(r, c):
            """ Extract a 3x3 subgrid from (r, c) """
            return [row[c:c+3] for row in grid[r:r+3]]
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        for r in range(rows - 2):
            for c in range(cols - 2):
                subgrid = extractSubgrid(r, c)
                if subgrid in magic_squares:
                    count += 1
        
        return count
