class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        prefix = [[0] * 26 for _ in range(n + 1)]  # Prefix frequency array for each letter
        
        # Step 1: Build the prefix frequency array
        for i in range(n):
            # Copy the previous frequencies
            prefix[i + 1] = prefix[i][:]
            # Update the frequency for the current character
            prefix[i + 1][ord(s[i]) - ord('a')] += 1
        
        # Step 2: Answer each query
        res = []
        for left, right, k in queries:
            # Calculate the frequency of each character in the substring s[left:right+1]
            odd_count = 0
            for i in range(26):
                freq_in_range = prefix[right + 1][i] - prefix[left][i]
                if freq_in_range % 2 != 0:
                    odd_count += 1
            
            # We can have at most (odd_count // 2) characters that need replacement
            # We can form a palindrome if (odd_count // 2) <= k
            if odd_count // 2 <= k:
                res.append(True)
            else:
                res.append(False)
        
        return res
