class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Recursive function to find the k-th symbol
        def find_symbol(n, k):
            # Base case
            if n == 1:
                return 0
            
            # Calculate the midpoint of the row
            midpoint = 2 ** (n - 2)
            
            if k <= midpoint:
                # k is in the first half
                return find_symbol(n - 1, k)
            else:
                # k is in the second half
                return 1 - find_symbol(n - 1, k - midpoint)
        
        return find_symbol(n, k)
