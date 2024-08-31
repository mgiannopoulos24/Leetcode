from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        def backtrack(r, c, index):
            # Base case: if index is equal to the length of word, we have found the word
            if index == len(word):
                return True
            
            # Out of bounds or character mismatch or already visited
            if (r < 0 or r >= len(board) or
                c < 0 or c >= len(board[0]) or
                board[r][c] != word[index]):
                return False
            
            # Mark the cell as visited
            temp, board[r][c] = board[r][c], '#'
            
            # Explore all possible directions
            found = (backtrack(r + 1, c, index + 1) or
                     backtrack(r - 1, c, index + 1) or
                     backtrack(r, c + 1, index + 1) or
                     backtrack(r, c - 1, index + 1))
            
            # Unmark the cell for the next potential path
            board[r][c] = temp
            
            return found
        
        # Start backtracking from every cell
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        
        return False