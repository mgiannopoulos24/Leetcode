class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        
        # Base case: if the text is empty, we cannot split anymore
        if n == 0:
            return 0
        
        # Try to find the longest matching prefix and suffix
        for i in range(1, n // 2 + 1):
            # Check if the first i characters match the last i characters
            if text[:i] == text[-i:]:
                # If they match, we have two identical parts
                # Count 2 (for this matching prefix and suffix) plus recurse on the middle part
                return 2 + self.longestDecomposition(text[i:-i])
        
        # If no such decomposition is possible, the entire string is one part
        return 1
