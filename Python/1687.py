class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        
        # Prefix sums for weights
        prefix_weight = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_weight[i] = prefix_weight[i - 1] + boxes[i - 1][1]
        
        # Track port visits
        trips = [0] * n
        for i in range(1, n):
            trips[i] = trips[i - 1]
            if boxes[i][0] != boxes[i - 1][0]:
                trips[i] += 1
        
        # Dynamic programming and sliding window
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        deque = collections.deque([0])  # Store indices of dp for valid transitions
        
        for i in range(1, n + 1):
            # Remove invalid transitions
            while deque and (i - deque[0] > maxBoxes or prefix_weight[i] - prefix_weight[deque[0]] > maxWeight):
                deque.popleft()
            
            # Compute dp[i]
            if deque:
                j = deque[0]
                dp[i] = dp[j] + trips[i - 1] - trips[j] + 2  # Add trips for ports and return to storage
            
            # Maintain deque monotonicity
            while deque and dp[i] <= dp[deque[-1]]:
                deque.pop()
            deque.append(i)
        
        return dp[n]
