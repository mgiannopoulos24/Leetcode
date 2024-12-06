class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        
        # Use two pointers to merge the words in lexicographically largest order
        while word1 and word2:
            # Choose from word1 if it is lexicographically greater or equal to word2
            if word1 > word2:
                merge.append(word1[0])
                word1 = word1[1:]
            else:
                merge.append(word2[0])
                word2 = word2[1:]
        
        # Append the remaining characters of the non-empty word
        merge.append(word1)
        merge.append(word2)
        
        # Join the list into a string
        return ''.join(merge)
