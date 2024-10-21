class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # Only need to check numbers up to 2^len(s)
        max_num_to_check = min(n, 2 ** len(s) - 1)
        
        for i in range(1, max_num_to_check + 1):
            binary_repr = bin(i)[2:]  # Get binary representation of i as a string
            if binary_repr not in s:
                return False
        
        return True
