import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and remove non-alphanumeric characters
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        # Check if the cleaned string is equal to its reverse
        return cleaned == cleaned[::-1]
