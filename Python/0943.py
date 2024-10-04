class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        
        # Function to calculate the maximum overlap between two words
        def calc_overlap(word1, word2):
            max_overlap = 0
            for i in range(1, len(word1) + 1):
                if word2.startswith(word1[-i:]):
                    max_overlap = i
            return max_overlap
        
        # Precompute the overlap between every pair of words
        overlaps = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    overlaps[i][j] = calc_overlap(words[i], words[j])
        
        # dp[mask][i] will store the minimum length superstring ending with word i and using all words in mask
        dp = [[float('inf')] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]
        
        # Initialize dp for each word
        for i in range(n):
            dp[1 << i][i] = len(words[i])
        
        # Fill dp table
        for mask in range(1 << n):
            for i in range(n):
                if mask & (1 << i):  # If i is in the current mask
                    prev_mask = mask ^ (1 << i)  # Remove i from the mask
                    for j in range(n):
                        if prev_mask & (1 << j):  # If j is in the previous mask
                            overlap = overlaps[j][i]
                            new_len = dp[prev_mask][j] + len(words[i]) - overlap
                            if new_len < dp[mask][i]:
                                dp[mask][i] = new_len
                                parent[mask][i] = j
        
        # Find the minimum length superstring that uses all words
        min_len = float('inf')
        last = -1
        final_mask = (1 << n) - 1
        for i in range(n):
            if dp[final_mask][i] < min_len:
                min_len = dp[final_mask][i]
                last = i
        
        # Reconstruct the superstring by backtracking the parent array
        result = []
        mask = final_mask
        while last != -1:
            result.append(last)
            next_last = parent[mask][last]
            mask ^= (1 << last)
            last = next_last
        
        result.reverse()
        
        # Build the final superstring using the result sequence
        superstring = words[result[0]]
        for k in range(1, len(result)):
            i, j = result[k-1], result[k]
            overlap = overlaps[i][j]
            superstring += words[j][overlap:]
        
        return superstring
