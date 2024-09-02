from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each letter in magazine and ransomNote
        magazine_count = Counter(magazine)
        ransomNote_count = Counter(ransomNote)
        
        # Check if magazine contains all the letters in ransomNote with sufficient counts
        for letter, count in ransomNote_count.items():
            if magazine_count[letter] < count:
                return False
        
        return True
