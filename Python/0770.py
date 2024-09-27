import collections

class Poly:
    def __init__(self):
        self.terms = collections.Counter()  # key is a tuple of variables, value is the coefficient

    @staticmethod
    def from_term(coef, vars):
        p = Poly()
        p.terms[tuple(sorted(vars))] = coef
        return p

    def __add__(self, other):
        result = Poly()
        result.terms = self.terms.copy()
        for term, coef in other.terms.items():
            result.terms[term] += coef
        return result

    def __sub__(self, other):
        result = Poly()
        result.terms = self.terms.copy()
        for term, coef in other.terms.items():
            result.terms[term] -= coef
        return result

    def __mul__(self, other):
        result = Poly()
        for term1, coef1 in self.terms.items():
            for term2, coef2 in other.terms.items():
                new_term = tuple(sorted(term1 + term2))
                result.terms[new_term] += coef1 * coef2
        return result

    def evaluate(self, evalmap):
        result = Poly()
        for term, coef in self.terms.items():
            new_term = []
            for var in term:
                if var in evalmap:
                    coef *= evalmap[var]
                else:
                    new_term.append(var)
            result.terms[tuple(new_term)] += coef
        return result

    def toList(self):
        result = []
        for term, coef in sorted(self.terms.items(), key=lambda x: (-len(x[0]), x[0])):
            if coef == 0:
                continue
            if len(term) == 0:
                result.append(str(coef))
            else:
                result.append(f"{coef}*{'*'.join(term)}")
        return result

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        evalmap = dict(zip(evalvars, evalints))

        def combine(left, right, symbol):
            if symbol == '+':
                return left + right
            elif symbol == '-':
                return left - right
            elif symbol == '*':
                return left * right

        def make(expr):
            if expr.isdigit() or (expr[0] == '-' and expr[1:].isdigit()):
                return Poly.from_term(int(expr), [])
            else:
                return Poly.from_term(1, [expr])

        def parse(expression):
            stack = []
            operand = []
            operators = []
            priority = 0
            ops_priority = {'+': 1, '-': 1, '*': 2}

            def collapse():
                right = stack.pop()
                left = stack.pop()
                op = operators.pop()
                stack.append(combine(left, right, op))

            for token in expression.replace('(', ' ( ').replace(')', ' ) ').split():
                if token == '(':
                    operators.append('(')
                elif token == ')':
                    while operators and operators[-1] != '(':
                        collapse()
                    operators.pop()  # remove '('
                elif token in ops_priority:
                    while (operators and operators[-1] in ops_priority and
                           ops_priority[token] <= ops_priority[operators[-1]]):
                        collapse()
                    operators.append(token)
                else:
                    stack.append(make(token))

            while operators:
                collapse()

            return stack[0]

        # Parse the expression into a polynomial
        poly = parse(expression)

        # Evaluate the polynomial with the evaluation map
        poly = poly.evaluate(evalmap)

        # Convert the polynomial into the required list format
        return poly.toList()
