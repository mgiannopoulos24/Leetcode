from collections import Counter
from functools import lru_cache

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        MOD = 10**9 + 7
        
        # Count frequency of each character in target
        target_count = Counter(target)
        
        # Preprocess stickers to only include characters in target
        sticker_counts = []
        for sticker in stickers:
            sticker_count = Counter(sticker)
            filtered_count = {char: sticker_count[char] for char in target_count if char in sticker_count}
            if filtered_count:
                sticker_counts.append(filtered_count)
        
        # Memoization for the recursive function
        @lru_cache(None)
        def dfs(remain):
            if not remain:
                return 0
            
            remain_count = Counter(remain)
            ans = float('inf')
            
            # Try each sticker to reduce the current remaining string
            for sticker_count in sticker_counts:
                # Skip if this sticker doesn't contain the first character of remain
                if sticker_count.get(remain[0], 0) == 0:
                    continue
                
                # Create a new remaining string after using this sticker
                new_remain = []
                for char in remain_count:
                    if remain_count[char] > sticker_count.get(char, 0):
                        new_remain.append(char * (remain_count[char] - sticker_count.get(char, 0)))
                
                new_remain = ''.join(new_remain)
                
                # Recursively find the minimum number of stickers needed for the new remaining string
                ans = min(ans, 1 + dfs(new_remain))
            
            return ans
        
        # Start the recursion with the full target
        result = dfs(target)
        return result if result != float('inf') else -1
