from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert wordList to a set for O(1) lookups
        wordSet = set(wordList)
        
        # If endWord is not in wordList, return 0 immediately
        if endWord not in wordSet:
            return 0
        
        # Initialize the queue with the beginWord and the initial length of the path
        queue = deque([(beginWord, 1)])
        
        while queue:
            current_word, current_length = queue.popleft()
            
            # Try all possible single-letter transformations
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = current_word[:i] + c + current_word[i+1:]
                    
                    if new_word == endWord:
                        return current_length + 1
                    
                    if new_word in wordSet:
                        # Add new_word to queue and remove it from set to avoid revisiting
                        queue.append((new_word, current_length + 1))
                        wordSet.remove(new_word)
        
        # Return 0 if no transformation sequence is found
        return 0
