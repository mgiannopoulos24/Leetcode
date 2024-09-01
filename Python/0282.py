class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        results = []
        if not num:
            return results
        self.backtrack(num, target, 0, 0, 0, "", results)
        return results

    def backtrack(self, num: str, target: int, index: int, prev_operand: int, current_value: int, expression: str, results: list[str]):
        if index == len(num):
            if current_value == target:
                results.append(expression)
            return
        
        for i in range(index, len(num)):
            # Skip leading zero numbers
            if i > index and num[index] == '0':
                break
            
            current_num_str = num[index:i + 1]
            current_num = int(current_num_str)
            
            if index == 0:
                # Start of the expression
                self.backtrack(num, target, i + 1, current_num, current_num, current_num_str, results)
            else:
                # Try all operations
                self.backtrack(num, target, i + 1, current_num, current_value + current_num, expression + "+" + current_num_str, results)
                self.backtrack(num, target, i + 1, -current_num, current_value - current_num, expression + "-" + current_num_str, results)
                self.backtrack(num, target, i + 1, prev_operand * current_num, (current_value - prev_operand) + (prev_operand * current_num), expression + "*" + current_num_str, results)
