class Solution:
    def minInsertions(self, s: str) -> int:
        left_parens = 0  # Number of unmatched '('
        insertions = 0   # Number of insertions required
        i = 0
        
        while i < len(s):
            if s[i] == '(':
                # An unmatched '(' is found, increase the count
                left_parens += 1
                i += 1
            else:
                # If we find ')', we want to check if we have two consecutive ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    # Valid pair of two consecutive ')'
                    i += 2
                else:
                    # Only one ')' found, we need to insert one more ')'
                    insertions += 1
                    i += 1
                
                # If we had a matching '(' for the '))', use it
                if left_parens > 0:
                    left_parens -= 1
                else:
                    # No matching '(', so we need to insert one '('
                    insertions += 1
        
        # After processing all characters, each unmatched '(' needs two ')'
        insertions += left_parens * 2
        
        return insertions
