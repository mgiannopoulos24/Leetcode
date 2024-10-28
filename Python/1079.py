from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Counter to keep track of tile frequencies
        tile_count = Counter(tiles)
        
        # Backtracking function to count possibilities
        def backtrack(counter):
            total_sequences = 0
            for tile in counter:
                if counter[tile] > 0:
                    # Choose the current tile
                    counter[tile] -= 1
                    
                    # Count this sequence and continue backtracking
                    total_sequences += 1 + backtrack(counter)
                    
                    # Backtrack (unchoose the tile)
                    counter[tile] += 1
            return total_sequences
        
        # Start backtracking with the counter
        return backtrack(tile_count)
