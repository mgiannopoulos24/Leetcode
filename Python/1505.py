class Solution:
    def minInteger(self, num: str, k: int) -> str:
        from collections import deque

        class FenwickTree:
            def __init__(self, size):
                self.n = size
                self.tree = [0] * (self.n + 1)

            def update(self, index, delta=1):
                while index <= self.n:
                    self.tree[index] += delta
                    index += index & -index

            def query(self, index):
                res = 0
                while index > 0:
                    res += self.tree[index]
                    index -= index & -index
                return res

        n = len(num)
        ft = FenwickTree(n)
        pos = {str(d): deque() for d in range(10)}
        for i, digit in enumerate(num):
            pos[digit].append(i)

        result = []
        for i in range(n):
            for d in range(10):
                if not pos[str(d)]:
                    continue
                idx = pos[str(d)][0]
                # Number of digits already moved before idx
                num_swaps = idx - ft.query(idx + 1)
                if num_swaps <= k:
                    k -= num_swaps
                    result.append(str(d))
                    ft.update(idx + 1)
                    pos[str(d)].popleft()
                    break
            else:
                # No break occurred, which shouldn't happen
                pass
            if k < 0:
                break
        return ''.join(result)
