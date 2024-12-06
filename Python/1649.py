class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index
    
    def query(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(instructions)
        
        # Initialize the Fenwick Tree (1-indexed for simplicity)
        fenwick = FenwickTree(max_val)
        total_cost = 0
        
        for i, num in enumerate(instructions):
            # Query the number of elements less than the current number
            less_count = fenwick.query(num - 1)
            # Query the number of elements greater than the current number
            greater_count = i - fenwick.query(num)
            
            # The cost is the minimum of elements less than or greater than the current number
            total_cost += min(less_count, greater_count)
            total_cost %= MOD
            
            # Update the Fenwick Tree with the current number
            fenwick.update(num, 1)
        
        return total_cost
