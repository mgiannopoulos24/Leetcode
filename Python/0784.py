from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(index: int, path: List[str]):
            # If we have processed all characters, add the result to the list
            if index == len(s):
                result.append("".join(path))
                return
            
            # Process the current character
            char = s[index]
            
            if char.isalpha():
                # If it's a letter, we have two choices: lowercase or uppercase
                path.append(char.lower())
                backtrack(index + 1, path)
                path.pop()
                
                path.append(char.upper())
                backtrack(index + 1, path)
                path.pop()
            else:
                # If it's a digit, we have only one choice
                path.append(char)
                backtrack(index + 1, path)
                path.pop()
        
        result = []
        backtrack(0, [])
        return result
