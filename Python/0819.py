import re
from collections import Counter
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Convert paragraph to lowercase
        paragraph = paragraph.lower()
        # Remove punctuation
        paragraph = re.sub(r'[!?\'\.,;]', ' ', paragraph)
        # Split paragraph into words
        words = paragraph.split()
        
        # Convert banned list to set for faster lookup
        banned_set = set(banned)
        
        # Count the frequency of each word, excluding banned words
        word_count = Counter(word for word in words if word not in banned_set)
        
        # Find the most common word
        most_common_word = word_count.most_common(1)[0][0]
        
        return most_common_word
