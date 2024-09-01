class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # Initialize the Trie with a root node

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create a new TrieNode if character is not present
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        return self._search_in_node(word, self.root)
    
    def _search_in_node(self, word: str, node: TrieNode) -> bool:
        if not word:
            return node.is_end_of_word
        
        char = word[0]
        if char == '.':
            # Try all possible children
            for child in node.children.values():
                if self._search_in_node(word[1:], child):
                    return True
        else:
            # Check the specific child
            if char in node.children:
                return self._search_in_node(word[1:], node.children[char])
        
        return False
