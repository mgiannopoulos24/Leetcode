class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search_shortest_root(self, word: str) -> str:
        node = self.root
        root = ""
        for char in word:
            if char in node.children:
                root += char
                node = node.children[char]
                if node.is_end_of_word:
                    return root
            else:
                break
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Build the Trie from the dictionary
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        
        # Replace words in the sentence
        words = sentence.split()
        replaced_words = [trie.search_shortest_root(word) for word in words]
        return " ".join(replaced_words)
