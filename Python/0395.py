class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def longest_substring_helper(s: str, k: int) -> int:
            # If the string length is less than k, it's impossible to have any valid substring
            if len(s) < k:
                return 0

            # Frequency count of each character in the string
            freq = {}
            for char in s:
                freq[char] = freq.get(char, 0) + 1

            # Find characters that have a frequency less than k
            for char, count in freq.items():
                if count < k:
                    # Split the string by this character and solve each part
                    return max(longest_substring_helper(part, k) for part in s.split(char))
            
            # If all characters have at least k frequency, return the length of the whole string
            return len(s)

        return longest_substring_helper(s, k)
