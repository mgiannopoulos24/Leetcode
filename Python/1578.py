class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        n = len(colors)
        
        # Iterate through the colors string
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                # If the consecutive balloons have the same color,
                # add the smaller removal time to total_time
                total_time += min(neededTime[i], neededTime[i - 1])
                # Keep the larger removal time as the time to keep the balloon
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        
        return total_time
