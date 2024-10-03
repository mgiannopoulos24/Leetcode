from collections import deque

class RecentCounter:

    def __init__(self):
        # Initialize an empty deque to store the timestamps of requests
        self.requests = deque()
        
    def ping(self, t: int) -> int:
        # Add the new request timestamp to the queue
        self.requests.append(t)
        
        # Remove requests that are outside the [t - 3000, t] window
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        
        # The number of requests within the last 3000 milliseconds is the size of the deque
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)