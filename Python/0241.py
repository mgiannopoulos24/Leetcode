from typing import List
import operator

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left: List[int], right: List[int], op: str) -> List[int]:
            ops = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul
            }
            return [ops[op](l, r) for l in left for r in right]
        
        def ways(expression: str) -> List[int]:
            if expression.isdigit():
                return [int(expression)]
            
            if expression in memo:
                return memo[expression]
            
            results = []
            for i, char in enumerate(expression):
                if char in '+-*':
                    left_results = ways(expression[:i])
                    right_results = ways(expression[i+1:])
                    results.extend(compute(left_results, right_results, char))
            
            memo[expression] = results
            return results
        
        memo = {}
        return ways(expression)
