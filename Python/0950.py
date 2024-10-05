from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # Sort the deck in ascending order
        deck.sort()
        
        # Initialize a deque to build the result
        result = deque()
        
        # Process each card starting from the end of the sorted deck
        for card in deck[::-1]:
            if result:
                result.appendleft(result.pop())
            result.appendleft(card)
        
        # Convert the deque to a list and return
        return list(result)
