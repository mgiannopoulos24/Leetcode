class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        lengths = [1]  # lengths[0] is the length after 0 operations
        for i in range(n):
            lengths.append(lengths[i] * 2)
        
        def next_char(c):
            return 'a' if c == 'z' else chr(ord(c) + 1)
        
        def get_char(k, op_index):
            if op_index == -1:
                return 'a'
            if k <= lengths[op_index]:
                return get_char(k, op_index - 1)
            else:
                k_prime = k - lengths[op_index]
                c = get_char(k_prime, op_index - 1)
                if operations[op_index] == 0:
                    return c
                else:
                    return next_char(c)
        
        return get_char(k, n - 1)
