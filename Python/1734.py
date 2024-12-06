from typing import List

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        
        # Step 1: Calculate total_xor for all numbers from 1 to n
        total_xor = 0
        for i in range(1, n + 1):
            total_xor ^= i
        
        # Step 2: Calculate XOR of encoded elements at even indices
        encoded_xor = 0
        for i in range(1, len(encoded), 2):
            encoded_xor ^= encoded[i]
        
        # Step 3: Calculate perm[0] as total_xor XOR encoded_xor
        perm = [total_xor ^ encoded_xor]
        
        # Step 4: Use perm[0] and encoded to reconstruct perm
        for i in range(len(encoded)):
            perm.append(perm[-1] ^ encoded[i])
        
        return perm
