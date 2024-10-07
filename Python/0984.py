class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []

        while a > 0 or b > 0:
            # Decide whether to append 'a' or 'b'
            if len(result) >= 2 and result[-1] == result[-2]:
                # If the last two characters are the same, append the other character
                if result[-1] == 'a':
                    result.append('b')
                    b -= 1
                else:
                    result.append('a')
                    a -= 1
            else:
                # Otherwise, append the character which has more remaining count
                if a >= b:
                    result.append('a')
                    a -= 1
                else:
                    result.append('b')
                    b -= 1

        return ''.join(result)
