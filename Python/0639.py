class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # Base case: at the start we have 1 way to decode an empty string
        prev1, prev2 = 1, 1  # prev1 is dp[i-1], prev2 is dp[i-2]
        
        for i in range(len(s)):
            curr = 0
            
            # Single character decoding
            if s[i] == '*':
                curr += 9 * prev1  # '*' can be '1' to '9'
            elif s[i] != '0':
                curr += prev1  # Non-zero single digit character
            
            # Two character decoding (previous character + current character)
            if i > 0:
                if s[i-1] == '1':
                    if s[i] == '*':
                        curr += 9 * prev2  # "1*" can be "11" to "19"
                    else:
                        curr += prev2  # "1X" is valid for X in [0-9]
                elif s[i-1] == '2':
                    if s[i] == '*':
                        curr += 6 * prev2  # "2*" can be "21" to "26"
                    elif s[i] <= '6':
                        curr += prev2  # "2X" is valid for X in [0-6]
                elif s[i-1] == '*':
                    if s[i] == '*':
                        curr += 15 * prev2  # "**" can be "11" to "19" or "21" to "26"
                    elif s[i] <= '6':
                        curr += 2 * prev2  # "*X" where X in [0-6] is "1X" or "2X"
                    else:
                        curr += prev2  # "*X" where X in [7-9] is only "1X"
            
            # Update previous values for next iteration
            curr %= MOD
            prev1, prev2 = curr, prev1
        
        return prev1
