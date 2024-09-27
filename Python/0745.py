from typing import List

class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix_suffix_map = {}
        
        for index, word in enumerate(words):
            # Create all possible prefix and suffix pairs for the word
            for i in range(len(word) + 1):
                for j in range(len(word) + 1):
                    prefix = word[:i]
                    suffix = word[-j:] if j != 0 else ""
                    self.prefix_suffix_map[(prefix, suffix)] = index

    def f(self, pref: str, suff: str) -> int:
        # Return the index of the word that matches the prefix and suffix
        return self.prefix_suffix_map.get((pref, suff), -1)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)