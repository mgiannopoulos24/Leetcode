class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store children nodes
        self.is_end_of_word = False  # Flag to mark the end of a word


class Trie:
    
    def __init__(self):
        self.root = TrieNode()  # Initialize the Trie with a root node

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Insert the character if not present
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # If character not found, word doesn't exist
            node = node.children[char]
        return node.is_end_of_word  # Check if it's the end of the word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False  # If character not found, prefix doesn't exist
            node = node.children[char]
        return True  # All characters in the prefix are found
