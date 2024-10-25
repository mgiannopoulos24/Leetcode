from collections import deque
from typing import List

class StreamChecker:
    def __init__(self, words: List[str]):
        # Initialize a Trie root
        self.trie = {}
        # Max length of any word in the input
        self.max_len = 0
        
        # Build the Trie with reversed words
        for word in words:
            node = self.trie
            self.max_len = max(self.max_len, len(word))
            for char in reversed(word):
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = True  # Mark the end of a word
        
        # Initialize a deque to store the stream of characters (up to max_len)
        self.stream = deque()

    def query(self, letter: str) -> bool:
        # Add the new character to the stream buffer
        self.stream.appendleft(letter)
        
        # Cap the size of the stream to max_len (remove the oldest character if necessary)
        if len(self.stream) > self.max_len:
            self.stream.pop()
        
        # Check if any suffix of the current stream is in the Trie
        node = self.trie
        for char in self.stream:
            if char not in node:
                return False
            node = node[char]
            if '#' in node:
                return True
        
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)