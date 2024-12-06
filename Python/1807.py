from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Convert knowledge list to a dictionary for O(1) lookups
        knowledge_dict = {key: value for key, value in knowledge}
        
        result = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                # Start of a key, find the end bracket
                j = i + 1
                while s[j] != ')':
                    j += 1
                # Extract the key
                key = s[i + 1:j]
                # Append the corresponding value or "?" if not found
                result.append(knowledge_dict.get(key, "?"))
                # Move i to the character after the closing bracket
                i = j + 1
            else:
                # Append regular characters directly to result
                result.append(s[i])
                i += 1
        
        # Join all parts to form the final evaluated string
        return "".join(result)
