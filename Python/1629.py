class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        # Initialize the maximum duration with the first key press
        max_duration = releaseTimes[0]
        result_key = keysPressed[0]
        
        # Iterate over all keys starting from the second one
        for i in range(1, len(keysPressed)):
            # Calculate the duration for the current key press
            duration = releaseTimes[i] - releaseTimes[i - 1]
            
            # Update the result if the current duration is longer,
            # or if it's equal and the current key is lexicographically larger
            if duration > max_duration or (duration == max_duration and keysPressed[i] > result_key):
                max_duration = duration
                result_key = keysPressed[i]
        
        return result_key
