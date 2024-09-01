class Solution:
    def calculate(self, s: str) -> int:
        def apply_op(ops, num, op):
            if op == '+':
                ops.append(num)
            elif op == '-':
                ops.append(-num)
            elif op == '*':
                ops[-1] *= num
            elif op == '/':
                # Truncate toward zero
                if ops[-1] // num < 0 and ops[-1] % num != 0:
                    ops[-1] = ops[-1] // num + 1
                else:
                    ops[-1] = ops[-1] // num

        ops = []
        num = 0
        op = '+'
        n = len(s)
        
        i = 0
        while i < n:
            char = s[i]
            
            if char.isdigit():
                num = num * 10 + int(char)
            
            if char in '+-*/' or i == n - 1:
                if char in '+-*/' or i == n - 1:
                    apply_op(ops, num, op)
                    num = 0
                    op = char

            i += 1
        
        return sum(ops)
