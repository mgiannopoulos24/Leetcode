class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        from collections import defaultdict
        import bisect

        # Step 1: Build the character index dictionary
        char_indices = defaultdict(list)
        for i, char in enumerate(s):
            char_indices[char].append(i)
        
        def is_subsequence(word):
            # Step 2: Check if the word is a subsequence of s
            current_position = -1
            for char in word:
                if char not in char_indices:
                    return False
                indices = char_indices[char]
                # Find the first index in `indices` that is greater than `current_position`
                pos = bisect.bisect_right(indices, current_position)
                if pos == len(indices):
                    return False
                current_position = indices[pos]
            return True
        
        # Step 3: Count the number of valid subsequences
        return sum(1 for word in words if is_subsequence(word))
