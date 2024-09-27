from collections import defaultdict
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def multiply_dict(d, factor):
            for key in d:
                d[key] *= factor

        def merge_dict(d1, d2):
            for key, value in d2.items():
                d1[key] = d1.get(key, 0) + value

        def parse_formula(formula):
            stack = [defaultdict(int)]
            i = 0
            while i < len(formula):
                char = formula[i]
                
                if char == '(':
                    stack.append(defaultdict(int))
                    i += 1
                elif char == ')':
                    i += 1
                    i_start = i
                    while i < len(formula) and formula[i].isdigit():
                        i += 1
                    multiplier = int(formula[i_start:i]) if i > i_start else 1
                    temp = stack.pop()
                    multiply_dict(temp, multiplier)
                    merge_dict(stack[-1], temp)
                elif char.isupper():
                    i_start = i
                    i += 1
                    while i < len(formula) and formula[i].islower():
                        i += 1
                    atom = formula[i_start:i]
                    i_start = i
                    while i < len(formula) and formula[i].isdigit():
                        i += 1
                    count = int(formula[i_start:i]) if i > i_start else 1
                    stack[-1][atom] += count
                else:
                    i += 1

            return stack[0]

        atom_count = parse_formula(formula)
        sorted_atoms = sorted(atom_count.keys())
        result = []
        for atom in sorted_atoms:
            count = atom_count[atom]
            result.append(atom + (str(count) if count > 1 else ''))

        return ''.join(result)

