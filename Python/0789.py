class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # Your distance to the target
        your_distance = abs(target[0]) + abs(target[1])
        
        # Check each ghost's distance to the target
        for ghost in ghosts:
            ghost_distance = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            # If any ghost can reach the target before or at the same time as you, you can't escape
            if ghost_distance <= your_distance:
                return False
        
        # If no ghost can reach the target before you, you can escape
        return True
