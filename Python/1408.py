class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        
        # Loop through each pair of words
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break  # We can break since we only need to know it's a substring of at least one word
        
        return result