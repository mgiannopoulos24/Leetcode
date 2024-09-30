class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def transform(word: str) -> tuple:
            even_chars = []
            odd_chars = []
            for i in range(len(word)):
                if i % 2 == 0:
                    even_chars.append(word[i])
                else:
                    odd_chars.append(word[i])
            return (tuple(sorted(even_chars)), tuple(sorted(odd_chars)))
        
        unique_groups = set()
        for word in words:
            unique_groups.add(transform(word))
        
        return len(unique_groups)
