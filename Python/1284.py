from typing import List

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        total = m * n

        # Function to map the matrix to a bitmask
        def mat_to_bitmask(mat):
            bitmask = 0
            for i in range(m):
                for j in range(n):
                    if mat[i][j]:
                        pos = i * n + j
                        bitmask |= (1 << pos)
            return bitmask

        # Precompute flip masks for each cell
        flip_masks = []
        for i in range(m):
            for j in range(n):
                mask = 0
                pos = i * n + j
                mask |= (1 << pos)
                # Up
                if i > 0:
                    mask |= (1 << ((i-1)*n + j))
                # Down
                if i < m -1:
                    mask |= (1 << ((i+1)*n + j))
                # Left
                if j > 0:
                    mask |= (1 << (i*n + (j-1)))
                # Right
                if j < n -1:
                    mask |= (1 << (i*n + (j+1)))
                flip_masks.append(mask)

        initial = mat_to_bitmask(mat)
        if initial == 0:
            return 0

        min_flips = float('inf')
        for flip_comb in range(1 << total):
            current = initial
            for k in range(total):
                if flip_comb & (1 << k):
                    current ^= flip_masks[k]
            if current == 0:
                flips = bin(flip_comb).count('1')
                if flips < min_flips:
                    min_flips = flips

        return min_flips if min_flips != float('inf') else -1
