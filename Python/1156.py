from collections import defaultdict

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # Step 1: Count the frequency of each character in the string
        freq = defaultdict(int)
        for ch in text:
            freq[ch] += 1
        
        # Step 2: Identify the consecutive segments for each character
        segments = []
        n = len(text)
        i = 0
        while i < n:
            ch = text[i]
            j = i
            while j < n and text[j] == ch:
                j += 1
            # Store (char, start index, length of segment)
            segments.append((ch, i, j - i))
            i = j
        
        # Step 3: Evaluate the maximum possible length for repeated characters
        max_len = 0
        
        # Traverse the segments and try extending/merging
        for i, (ch, start, length) in enumerate(segments):
            # Option 1: Take the length of the current segment and extend by one
            max_len = max(max_len, length + (1 if freq[ch] > length else 0))
            
            # Option 2: Merge with the next segment if there is exactly one different character between them
            if i + 2 < len(segments) and segments[i + 2][0] == ch and segments[i + 1][2] == 1:
                # We have a form like: chaaaach
                merged_length = length + segments[i + 2][2]
                # Can merge + take 1 more character if there are more left of this type
                max_len = max(max_len, merged_length + (1 if freq[ch] > merged_length else 0))
        
        return max_len
