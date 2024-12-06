class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # Map each letter to its corresponding (row, col) on the board
        board_map = {chr(i + ord('a')): (i // 5, i % 5) for i in range(26)}
        
        # Start position at (0, 0)
        curr_row, curr_col = 0, 0
        result = []
        
        for char in target:
            # Get the target position of the current character
            target_row, target_col = board_map[char]
            
            # Handle moving to 'z' carefully: Move horizontally first if moving to 'z'
            if char == 'z':
                # Move horizontally first to avoid out-of-bounds issues
                while curr_col > target_col:
                    result.append('L')
                    curr_col -= 1
                while curr_col < target_col:
                    result.append('R')
                    curr_col += 1
                while curr_row < target_row:
                    result.append('D')
                    curr_row += 1
            
            # Handle moving away from 'z' carefully: Move up first if moving away from 'z'
            elif curr_row == 5 and curr_col == 0:
                # Move up first before horizontal movement
                while curr_row > target_row:
                    result.append('U')
                    curr_row -= 1
                while curr_col < target_col:
                    result.append('R')
                    curr_col += 1
            else:
                # First move up or down
                while curr_row > target_row:
                    result.append('U')
                    curr_row -= 1
                while curr_row < target_row:
                    result.append('D')
                    curr_row += 1
                
                # Then move left or right
                while curr_col > target_col:
                    result.append('L')
                    curr_col -= 1
                while curr_col < target_col:
                    result.append('R')
                    curr_col += 1

            # Add '!' to mark the character is selected
            result.append('!')
        
        return ''.join(result)
