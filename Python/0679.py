from itertools import permutations, product

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def evaluate(a: float, b: float, op: str) -> float:
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            elif op == '/':
                if b == 0:
                    return float('inf')  # Avoid division by zero
                return a / b
            return 0

        def valid(expression: float) -> bool:
            # Check if the result is approximately 24
            return abs(expression - 24) < 1e-6

        def backtrack(nums: List[float]) -> bool:
            n = len(nums)
            if n == 1:
                return valid(nums[0])
            
            for i in range(n):
                for j in range(i + 1, n):
                    # Combine nums[i] and nums[j] with all operators
                    for op in ['+', '-', '*', '/']:
                        new_nums = []
                        for k in range(n):
                            if k != i and k != j:
                                new_nums.append(nums[k])
                        new_nums.append(evaluate(nums[i], nums[j], op))
                        if backtrack(new_nums):
                            return True

                    # Combine nums[j] and nums[i] with all operators (in case of non-commutative ops)
                    for op in ['+', '-', '*', '/']:
                        new_nums = []
                        for k in range(n):
                            if k != i and k != j:
                                new_nums.append(nums[k])
                        new_nums.append(evaluate(nums[j], nums[i], op))
                        if backtrack(new_nums):
                            return True
            return False

        # Try all permutations of numbers
        for num_perm in permutations(cards):
            if backtrack(list(num_perm)):
                return True

        return False
