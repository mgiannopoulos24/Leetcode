class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        seen = set()  # To store unique echo substrings
        
        # Iterate through all possible substrings
        for length in range(2, n + 1, 2):  # Only consider even lengths
            for i in range(n - length + 1):
                mid = i + length // 2
                # Check if the first half is equal to the second half
                if text[i:mid] == text[mid:i+length]:
                    seen.add(text[i:i+length])
        
        return len(seen)
