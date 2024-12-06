class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        total_count = 0

        # Sliding window over the string
        for start in range(n):
            vowel_set = set()  # To track unique vowels in the window
            consonant_count = 0  # To count consonants in the window
            
            for end in range(start, n):
                char = word[end]
                
                # Check if the character is a vowel or consonant
                if char in vowels:
                    vowel_set.add(char)
                else:
                    consonant_count += 1
                
                # If the number of consonants exceeds k, break early
                if consonant_count > k:
                    break
                
                # Check if we have all the vowels and exactly k consonants
                if len(vowel_set) == 5 and consonant_count == k:
                    total_count += 1
        
        return total_count
