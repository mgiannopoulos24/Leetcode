class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # Sort clips by start time, and for ties, by the farthest end time
        clips.sort(key=lambda x: (x[0], x[1]))
        
        count = 0
        current_end = 0
        farthest = 0
        i = 0
        n = len(clips)
        
        while i < n and current_end < time:
            # Check if there's a gap we can't cover
            if clips[i][0] > current_end:
                return -1
            
            # Find the clip that extends our current coverage the furthest
            while i < n and clips[i][0] <= current_end:
                farthest = max(farthest, clips[i][1])
                i += 1
            
            # We must take this clip to extend our coverage
            count += 1
            current_end = farthest
            
            # If we have covered the required time, stop
            if current_end >= time:
                return count
        
        # If we finish the loop and haven't covered the whole time, return -1
        return -1 if current_end < time else count
