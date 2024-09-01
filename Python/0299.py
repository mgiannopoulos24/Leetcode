class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Initialize counts for bulls and cows
        bulls = 0
        cows = 0
        
        # Counters for digits in secret and guess
        secret_count = [0] * 10
        guess_count = [0] * 10
        
        # First pass: find bulls and count digits
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                # Increment the count for digits that are not bulls
                secret_count[int(s)] += 1
                guess_count[int(g)] += 1
        
        # Second pass: calculate cows based on the counts
        for i in range(10):
            cows += min(secret_count[i], guess_count[i])
        
        return f"{bulls}A{cows}B"
