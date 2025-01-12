class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(answerKey: str, k: int, target: str) -> int:
            left = 0
            max_len = 0
            changes = 0
            
            for right in range(len(answerKey)):
                if answerKey[right] != target:
                    changes += 1
                
                while changes > k:
                    if answerKey[left] != target:
                        changes -= 1
                    left += 1
                
                max_len = max(max_len, right - left + 1)
            
            return max_len
        
        # Calculate the maximum consecutive 'T's by changing at most k 'F's to 'T's
        max_T = maxConsecutiveChar(answerKey, k, 'T')
        
        # Calculate the maximum consecutive 'F's by changing at most k 'T's to 'F's
        max_F = maxConsecutiveChar(answerKey, k, 'F')
        
        return max(max_T, max_F)