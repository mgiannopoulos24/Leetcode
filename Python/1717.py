class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Determine which pair to prioritize based on the points
        first, second, first_points, second_points = ("ab", "ba", x, y) if x >= y else ("ba", "ab", y, x)
        
        # Helper function to remove pairs and calculate points
        def remove_pairs(s, pair, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] + char == pair:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score

        # Remove the prioritized pair first
        remaining_string, score = remove_pairs(s, first, first_points)
        # Remove the other pair from the remaining string
        _, additional_score = remove_pairs(remaining_string, second, second_points)
        
        return score + additional_score
