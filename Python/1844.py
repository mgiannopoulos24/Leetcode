class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c: str, x: int) -> str:
            return chr(ord(c) + x)

        result = []
        for i in range(len(s)):
            if i % 2 == 0:
                result.append(s[i])
            else:
                result.append(shift(s[i - 1], int(s[i])))

        return "".join(result)