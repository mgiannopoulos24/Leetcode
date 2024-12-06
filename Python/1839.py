class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        max_length = 0
        current_length = 0
        vowel_count = 0
        vowels = "aeiou"
        
        for i in range(len(word)):
            # Check if current character follows the sorted order or is the same as previous
            if i > 0 and word[i] < word[i - 1]:
                # Reset counters if the order is broken
                current_length = 0
                vowel_count = 0
            
            # Increment current length as the character is part of a valid sequence
            current_length += 1
            
            # Count a new vowel only when it differs from the previous character
            if i == 0 or word[i] != word[i - 1]:
                if word[i] == vowels[vowel_count]:
                    vowel_count += 1
            
            # Check if this substring is beautiful
            if vowel_count == 5:
                max_length = max(max_length, current_length)
        
        return max_length
