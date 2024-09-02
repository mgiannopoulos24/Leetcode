from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None, None]  # Array of size 2 for bit 0 and 1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.children[bit] is None:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def find_max_xor(self, num):
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit
            if node.children[toggled_bit] is not None:
                max_xor = (max_xor << 1) | 1
                node = node.children[toggled_bit]
            else:
                max_xor = (max_xor << 1) | 0
                node = node.children[bit]
        return max_xor

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        max_xor = 0
        for num in nums:
            trie.insert(num)
            max_xor = max(max_xor, trie.find_max_xor(num))
        return max_xor
