from math import comb

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        row, column = destination
        path = []
        
        # We need exactly `row` V moves and `column` H moves
        for _ in range(row + column):
            if column > 0:
                # Compute the number of paths if we choose 'H' as the next move
                num_ways_with_H = comb(row + column - 1, column - 1)
                
                if k <= num_ways_with_H:
                    # If k is within the number of paths that start with 'H'
                    path.append('H')
                    column -= 1  # We used one 'H'
                else:
                    # If k is larger, we choose 'V' and decrease k accordingly
                    path.append('V')
                    row -= 1  # We used one 'V'
                    k -= num_ways_with_H  # Adjust k for the remaining paths
            else:
                # If there are no more 'H's left, we must use 'V'
                path.append('V')
                row -= 1
        
        return ''.join(path)
