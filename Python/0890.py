class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matches(word, pattern):
            if len(word) != len(pattern):
                return False
            
            map_word_to_pattern = {}
            map_pattern_to_word = {}
            
            for w, p in zip(word, pattern):
                if w not in map_word_to_pattern:
                    map_word_to_pattern[w] = p
                if p not in map_pattern_to_word:
                    map_pattern_to_word[p] = w
                
                if map_word_to_pattern[w] != p or map_pattern_to_word[p] != w:
                    return False
            
            return True
        
        return [word for word in words if matches(word, pattern)]
