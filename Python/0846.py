from typing import List
from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If the total number of cards is not divisible by groupSize, return False
        if len(hand) % groupSize != 0:
            return False
        
        # Count the frequency of each card
        freq = defaultdict(int)
        for card in hand:
            freq[card] += 1
        
        # Sort the unique cards
        sorted_cards = sorted(freq.keys())
        
        # Try to form groups
        for card in sorted_cards:
            while freq[card] > 0:  # While there are still cards of this value
                # Check if the next (groupSize - 1) consecutive cards exist
                for i in range(1, groupSize):
                    if freq[card + i] < freq[card]:
                        return False
                # Reduce the frequency of the cards in this group
                for i in range(groupSize):
                    freq[card + i] -= 1
        
        return True