class TrieNode:
    def __init__(self):
        self.children = {}
        self.sum = 0  # Sum of values of all keys with this node as a prefix

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, key: str, value: int) -> None:
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sum += value  # Update the sum for each node in the path
    
    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.sum

class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.key_to_value = {}  # To keep track of the actual values for keys
    
    def insert(self, key: str, val: int) -> None:
        if key in self.key_to_value:
            old_val = self.key_to_value[key]
        else:
            old_val = 0
        
        self.key_to_value[key] = val
        # Insert or update in the Trie with the difference
        self.trie.insert(key, val - old_val)
    
    def sum(self, prefix: str) -> int:
        return self.trie.sum(prefix)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)