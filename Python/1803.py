from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num: int):
        node = self.root
        for i in range(14, -1, -1):  # 15 bits for numbers up to 2 * 10^4
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1
    
    def countLessThanOrEqual(self, num: int, limit: int) -> int:
        node = self.root
        count = 0
        for i in range(14, -1, -1):
            if not node:
                break
            num_bit = (num >> i) & 1
            limit_bit = (limit >> i) & 1
            # Check if we can take the current path to satisfy XOR ≤ limit
            if limit_bit == 1:
                if num_bit in node.children:
                    count += node.children[num_bit].count
                node = node.children.get(1 - num_bit, None)
            else:
                node = node.children.get(num_bit, None)
        
        if node:
            count += node.count
        return count
    
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        total_pairs = 0
        for num in nums:
            total_pairs += self.countLessThanOrEqual(num, high) - self.countLessThanOrEqual(num, low - 1)
            self.insert(num)
        return total_pairs
