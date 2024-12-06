class Solution:
    def minimumDistance(self, word: str) -> int:
        # Precompute the coordinates for each letter 'A' to 'Z' on a 5x6 grid
        def get_pos(char):
            pos = ord(char) - ord('A')
            return (pos // 6, pos % 6)

        # Calculate Manhattan distance between two letters
        def dist(c1, c2):
            x1, y1 = get_pos(c1)
            x2, y2 = get_pos(c2)
            return abs(x1 - x2) + abs(y1 - y2)

        # Memoization for dp(i, f1, f2)
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(i, f1, f2):
            if i == len(word):  # Base case, no more letters to type
                return 0
            # Option 1: Use f1 to type the current letter (word[i])
            use_f1 = dp(i + 1, word[i], f2) + (0 if f1 == '' else dist(f1, word[i]))
            # Option 2: Use f2 to type the current letter (word[i])
            use_f2 = dp(i + 1, f1, word[i]) + (0 if f2 == '' else dist(f2, word[i]))
            return min(use_f1, use_f2)
        
        # Initialize the DP function with no fingers assigned yet
        return dp(0, '', '')
