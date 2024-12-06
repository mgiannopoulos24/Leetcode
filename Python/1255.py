from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        Returns the maximum score of any valid set of words formed by using the given letters.
        
        Args:
        words (List[str]): List of words.
        letters (List[str]): List of available letters.
        score (List[int]): List of scores for each letter 'a' to 'z'.
        
        Returns:
        int: The maximum score achievable.
        """
        # Precompute the frequency of each available letter
        available_letters = [0] * 26
        for letter in letters:
            available_letters[ord(letter) - ord('a')] += 1
        
        # Precompute the letter counts and scores for each word
        word_counts = []
        word_scores = []
        for word in words:
            count = [0] * 26
            total = 0
            for char in word:
                idx = ord(char) - ord('a')
                count[idx] += 1
                total += score[idx]
            word_counts.append(count)
            word_scores.append(total)
        
        n = len(words)
        max_score = 0
        
        # Iterate over all possible subsets using bitmasking
        for mask in range(1 << n):
            current_count = [0] * 26
            current_score = 0
            valid = True
            for i in range(n):
                if mask & (1 << i):
                    # Add word_counts[i] to current_count
                    for j in range(26):
                        current_count[j] += word_counts[i][j]
                        # Early termination if count exceeds available letters
                        if current_count[j] > available_letters[j]:
                            valid = False
                            break
                    if not valid:
                        break
                    current_score += word_scores[i]
            if valid:
                if current_score > max_score:
                    max_score = current_score
        return max_score
