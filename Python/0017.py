from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to letters
        phone_mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        
        def backtrack(combination, next_digits):
            # Base case: if there are no more digits to check
            if len(next_digits) == 0:
                results.append(combination)
            else:
                # Iterate over each letter which corresponds to the current digit
                for letter in phone_mapping[next_digits[0]]:
                    # Add the current letter to the combination and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
        
        results = []
        backtrack('', digits)
        return results