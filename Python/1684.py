class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Step 1: Convert allowed string into a set for O(1) lookup
        allowed_set = set(allowed)
        
        # Step 2: Initialize the counter for consistent strings
        consistent_count = 0
        
        # Step 3: Iterate through each word in the words list
        for word in words:
            # Step 4: Check if all characters in the word are in allowed_set
            if all(char in allowed_set for char in word):
                consistent_count += 1
        
        # Step 5: Return the total count of consistent strings
        return consistent_count
