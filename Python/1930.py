class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Store the first and last occurrence of each character
        first_occurrence = {}
        last_occurrence = {}
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i

        unique_palindromes = set()

        # Iterate over each character as the center of the palindrome
        for char, start in first_occurrence.items():
            end = last_occurrence[char]
            if end - start > 1:  # There are characters between start and end
                # Add all unique characters between start+1 and end-1
                middle_chars = set(s[start + 1:end])
                for mid_char in middle_chars:
                    unique_palindromes.add((char, mid_char, char))

        return len(unique_palindromes)
