from typing import List, Dict

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

    def search_prefix(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(x: int, y: int, node: TrieNode, path: str):
            if node.is_end_of_word:
                result.add(path)
                node.is_end_of_word = False  # Avoid duplicate entries

            if not (0 <= x < len(board) and 0 <= y < len(board[0])) or (x, y) in visited:
                return

            visited.add((x, y))
            char = board[x][y]
            if char not in node.children:
                visited.remove((x, y))
                return

            next_node = node.children[char]
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                dfs(nx, ny, next_node, path + char)

            visited.remove((x, y))

        # Step 1: Build the Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        # Step 2: Perform DFS from each cell in the board
        result = set()
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie.root, "")

        return list(result)
