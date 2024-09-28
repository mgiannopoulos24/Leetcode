class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        result = []
        
        for i, word in enumerate(words):
            if word[0].lower() in vowels:
                # Word starts with a vowel
                goat_word = word + "ma"
            else:
                # Word starts with a consonant
                goat_word = word[1:] + word[0] + "ma"
                
            # Add the suffix 'a' (i + 1) times
            goat_word += 'a' * (i + 1)
            
            result.append(goat_word)
        
        return ' '.join(result)
