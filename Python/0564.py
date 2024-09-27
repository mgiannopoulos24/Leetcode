class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        
        # Edge case for n = "1"
        if n == "1":
            return "0"
        
        # The first half (plus the middle digit if odd length)
        first_half = n[:(length + 1) // 2]
        first_half_num = int(first_half)
        
        # Generate three possible palindromes:
        # 1. Mirror the first_half.
        # 2. Mirror the first_half - 1.
        # 3. Mirror the first_half + 1.
        candidates = []
        
        # Convert the first half, the first half - 1, and the first half + 1 into palindromes
        for delta in [-1, 0, 1]:
            new_half = str(first_half_num + delta)
            if length % 2 == 0:
                palindrome = new_half + new_half[::-1]
            else:
                palindrome = new_half + new_half[:-1][::-1]
            candidates.append(palindrome)
        
        # Edge cases: all 9's or numbers like 1000, 10000, etc.
        candidates.append(str(10**(length - 1) - 1))  # Example: 999 -> 1000 -> 999
        candidates.append(str(10**length + 1))  # Example: 999 -> 1001
        
        # Remove the original number itself from the candidate list
        candidates = [c for c in candidates if c != n]
        
        # Convert candidates to integers, find the closest palindrome
        n_int = int(n)
        closest_palindrome = min(candidates, key=lambda x: (abs(int(x) - n_int), int(x)))
        
        return closest_palindrome
