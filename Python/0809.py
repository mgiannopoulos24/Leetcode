from typing import List
import itertools

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_groups(word: str):
            """Helper function to split word into character groups."""
            return [(char, len(list(group))) for char, group in itertools.groupby(word)]
        
        # Get the groups for the string s
        s_groups = get_groups(s)
        result = 0
        
        for word in words:
            word_groups = get_groups(word)
            
            # If the number of groups doesn't match, the word can't be stretchy
            if len(s_groups) != len(word_groups):
                continue
            
            stretchy = True
            for (s_char, s_count), (w_char, w_count) in zip(s_groups, word_groups):
                # Characters in corresponding groups must match
                if s_char != w_char:
                    stretchy = False
                    break
                
                # s group must either be the same size as w group or be stretchable
                if s_count < 3 and s_count != w_count:
                    stretchy = False
                    break
                
                if s_count >= 3 and s_count < w_count:
                    stretchy = False
                    break
            
            if stretchy:
                result += 1
        
        return result
