from typing import List
from collections import defaultdict

# Assuming the Master class is provided as per the problem statement.
# You should not implement or modify it.
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        """
        Attempts to guess the secret word by interacting with the Master API using the Minimax strategy.
        
        :param words: List of unique six-letter words.
        :param master: An instance of the Master class to make guesses.
        """
        
        def match(word1: str, word2: str) -> int:
            """
            Calculates the number of exact matches between two words.
            
            :param word1: First word.
            :param word2: Second word.
            :return: Number of matching characters in the same positions.
            """
            return sum(c1 == c2 for c1, c2 in zip(word1, word2))
        
        def select_guess(candidates: List[str]) -> str:
            """
            Selects the next guess using the Minimax strategy.
            
            :param candidates: Current list of candidate words.
            :return: The selected word to guess next.
            """
            min_max = float('inf')
            best_guess = candidates[0]
            
            for guess in candidates:
                # Dictionary to count the number of candidates for each possible match score
                count = defaultdict(int)
                for target in candidates:
                    if guess != target:
                        score = match(guess, target)
                        count[score] += 1
                # The worst-case scenario is the maximum group size for any match score
                worst_case = max(count.values(), default=0)
                if worst_case < min_max:
                    min_max = worst_case
                    best_guess = guess
            return best_guess
        
        # Initialize the candidate pool
        candidates = words.copy()
        
        for _ in range(30):  # Maximum of 30 allowed guesses
            if not candidates:
                break  # No candidates left to guess
            
            # Select the next guess using the Minimax strategy
            guess = select_guess(candidates)
            
            # Make the guess and get the number of matches
            matches = master.guess(guess)
            
            if matches == 6:
                return  # Secret word guessed correctly
            
            # Filter candidates based on the number of matches
            candidates = [word for word in candidates if match(guess, word) == matches]
        
        # If the secret word is not found within allowed guesses, do nothing
        return
