class MagicDictionary:
    def __init__(self):
        self.words_set = set()
    
    def buildDict(self, dictionary: List[str]) -> None:
        """ Set up the dictionary with the given list of words. """
        self.words_set = set(dictionary)
    
    def search(self, searchWord: str) -> bool:
        """ Check if we can change exactly one character to match any word in the dictionary. """
        # Check all words in the dictionary
        for word in self.words_set:
            if len(word) == len(searchWord):
                # Check if exactly one character differs
                diff_count = 0
                for i in range(len(word)):
                    if word[i] != searchWord[i]:
                        diff_count += 1
                    if diff_count > 1:
                        break
                if diff_count == 1:
                    return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)