from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, it's impossible
        if k > len(s):
            return False
        
        # Count the frequency of each character
        freq = Counter(s)
        
        # Count how many characters have odd frequencies
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        
        # We need at least `odd_count` palindromes (since each odd frequency can only be the center of one palindrome)
        # So if `odd_count` is greater than `k`, it's impossible to form `k` palindromes
        return odd_count <= k
