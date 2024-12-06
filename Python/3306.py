from collections import defaultdict
import bisect

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        last_vowel = {v: -1 for v in vowels}
        unique_vowels_present = 0
        prefix_consonants = 0
        result = 0
        
        # Mapping from prefix_consonants to list of indices where this prefix occurs
        prefix_map = defaultdict(list)
        prefix_map[0].append(0)  # Initialize with prefix_consonants=0 at index 0
        
        for right in range(n):
            char = word[right]
            
            # Update consonant count or vowel count
            if char not in vowels:
                prefix_consonants += 1
            else:
                # Update last occurrence of the vowel
                if last_vowel[char] == -1:
                    unique_vowels_present += 1
                last_vowel[char] = right
            
            # Check if all vowels have been seen
            if unique_vowels_present == 5:
                # Find the minimal start index to include all vowels
                min_start = min(last_vowel.values())
                
                # Calculate target prefix sum for exactly k consonants
                target_prefix = prefix_consonants - k
                
                if target_prefix in prefix_map:
                    # List of possible 'left' indices with prefix_consonants == target_prefix
                    left_indices = prefix_map[target_prefix]
                    
                    # Number of 'left' indices <= min_start
                    # Since left_indices are sorted, we can use binary search
                    count = bisect.bisect_right(left_indices, min_start)
                    result += count
            
            # Add current index+1 to prefix_map for the current prefix_consonants
            # This represents that prefix_consonants up to index+1 is current
            prefix_map[prefix_consonants].append(right + 1)
        
        return result
