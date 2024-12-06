class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        s = list(s)
        while len(s) > 1:
            if s[-1] == '0':
                # Even, divide by 2 by removing the last bit
                s.pop()
            else:
                # Odd, add 1 to the number
                self.add_one(s)
            steps += 1
        return steps

    def add_one(self, s):
        carry = 1
        i = len(s) - 1
        while i >= 0 and carry:
            if s[i] == '1':
                s[i] = '0'
                carry = 1
            else:
                s[i] = '1'
                carry = 0
            i -= 1
        if carry:
            s.insert(0, '1')
