class Solution:
    def reinitializePermutation(self, n: int) -> int:
        # Start with index 1 and count the number of operations
        index = 1
        operations = 0

        while True:
            if index % 2 == 0:
                index //= 2
            else:
                index = n // 2 + (index - 1) // 2
            
            operations += 1
            
            # If index returns to 1, the permutation is back to its initial state
            if index == 1:
                break
        
        return operations
