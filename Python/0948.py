class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()  # Sort the tokens
        left, right = 0, len(tokens) - 1  # Initialize two pointers
        score = 0  # Initial score
        max_score = 0  # Maximum score achievable
        
        while left <= right:
            if power >= tokens[left]:
                # Play token face-up
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                # Play token face-down
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                # No valid move can be made
                break
        
        return max_score
