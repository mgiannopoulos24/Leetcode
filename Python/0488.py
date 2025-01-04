from collections import deque

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
        # Helper function to remove consecutive balls starting from index i
        def remove_same(s, i):
            if i < 0:
                return s
            
            left = right = i
            while left > 0 and s[left-1] == s[i]:
                left -= 1
            while right+1 < len(s) and s[right+1] == s[i]:
                right += 1
            
            length = right - left + 1
            if length >= 3:
                new_s = s[:left] + s[right+1:]
                return remove_same(new_s, left-1)
            else:
                return s

        # Sort the hand for consistent state representation
        hand = "".join(sorted(hand))
        
        # Use a queue for BFS
        queue = deque()
        queue.append((board, hand, 0))
        
        # Use a set to track visited states
        visited = set()
        visited.add((board, hand))
        
        while queue:
            current_board, current_hand, steps = queue.popleft()
            
            # Try inserting each ball in the hand at every possible position
            for i in range(len(current_board) + 1):
                for j in range(len(current_hand)):
                    # Skip if the current ball is the same as the previous one in the hand
                    if j > 0 and current_hand[j] == current_hand[j-1]:
                        continue
                    
                    # Skip if inserting this ball doesn't help form a group
                    if i > 0 and current_board[i-1] == current_hand[j]:
                        continue
                    
                    pick = False
                    # Check if the ball can be picked to form a group
                    if i < len(current_board) and current_board[i] == current_hand[j]:
                        pick = True
                    if 0 < i < len(current_board) and current_board[i-1] == current_board[i] and current_board[i] != current_hand[j]:
                        pick = True
                    
                    if pick:
                        # Insert the ball and reduce the board
                        new_board = remove_same(current_board[:i] + current_hand[j] + current_board[i:], i)
                        new_hand = current_hand[:j] + current_hand[j+1:]
                        
                        # If the board is empty, return the number of steps
                        if not new_board:
                            return steps + 1
                        
                        # If this state hasn't been visited, add it to the queue
                        if (new_board, new_hand) not in visited:
                            visited.add((new_board, new_hand))
                            queue.append((new_board, new_hand, steps + 1))
        
        # If no solution found
        return -1