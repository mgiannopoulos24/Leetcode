class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        current_winner = arr[0]
        win_count = 0
        
        for i in range(1, len(arr)):
            if current_winner > arr[i]:
                win_count += 1
            else:
                current_winner = arr[i]
                win_count = 1
            
            # If current_winner wins k times consecutively, return it
            if win_count == k:
                return current_winner
        
        # If no one wins k times consecutively, the largest element will eventually win
        return current_winner
