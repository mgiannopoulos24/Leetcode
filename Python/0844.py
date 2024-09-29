class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(st: str) -> str:
            result = []
            for char in st:
                if char == '#':
                    if result:
                        result.pop()  # Remove the last character if there's one to remove
                else:
                    result.append(char)
            return result
        
        return process_string(s) == process_string(t)
