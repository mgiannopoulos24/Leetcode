class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort words by their length
        words.sort(key=len)
        
        # Dictionary to store the longest chain ending at each word
        dp = {}
        
        max_chain_length = 1  # The minimum chain length is 1 (the word itself)
        
        for word in words:
            dp[word] = 1  # Every word is at least a chain of length 1 (itself)
            
            # Generate all possible predecessors by removing one character
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                
                if predecessor in dp:
                    # If the predecessor exists, update the chain length for the current word
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            
            # Update the maximum chain length
            max_chain_length = max(max_chain_length, dp[word])
        
        return max_chain_length
