from typing import List
import bisect

class TrieNode:
    def __init__(self):
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num: int) -> None:
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
    
    def find_max_xor(self, num: int) -> int:
        node = self.root
        if not node.children:  # If the Trie is empty
            return -1
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit
            if toggled_bit in node.children:
                max_xor = (max_xor << 1) | 1
                node = node.children[toggled_bit]
            else:
                max_xor = (max_xor << 1)
                node = node.children.get(bit, node)
        return max_xor

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()  # Sort nums to efficiently manage elements up to mi
        indexed_queries = sorted([(xi, mi, i) for i, (xi, mi) in enumerate(queries)], key=lambda x: x[1])
        answer = [-1] * len(queries)
        trie = Trie()
        idx = 0  # To iterate over nums
        
        for xi, mi, q_idx in indexed_queries:
            # Add nums[j] <= mi to Trie
            while idx < len(nums) and nums[idx] <= mi:
                trie.insert(nums[idx])
                idx += 1
            # Find max XOR for current xi
            answer[q_idx] = trie.find_max_xor(xi)
        
        return answer
