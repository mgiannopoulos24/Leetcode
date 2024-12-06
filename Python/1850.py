class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def get_next_permutation(s):
            s = list(s)
            n = len(s)
            i = n - 2

            while i >= 0 and s[i] >= s[i + 1]:
                i -= 1

            if i >= 0:
                j = n - 1
                while s[j] <= s[i]:
                    j -= 1
                s[i], s[j] = s[j], s[i]

            s = s[:i + 1] + s[i + 1:][::-1]
            return ''.join(s)

        target = num
        for _ in range(k):
            target = get_next_permutation(target)

        num = list(num)
        target = list(target)
        swaps = 0

        for i in range(len(num)):
            if num[i] != target[i]:
                j = i
                while num[j] != target[i]:
                    j += 1

                while j > i:
                    num[j], num[j - 1] = num[j - 1], num[j]
                    j -= 1
                    swaps += 1

        return swaps
