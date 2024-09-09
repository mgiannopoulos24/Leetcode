from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Queues for Radiant and Dire senators
        radiant_queue = deque()
        dire_queue = deque()
        
        # Initialize queues with the indices of senators from each party
        for index, senator in enumerate(senate):
            if senator == 'R':
                radiant_queue.append(index)
            else:
                dire_queue.append(index)
        
        # Simulate the rounds of voting
        while radiant_queue and dire_queue:
            # Get the indices of the front senators from each queue
            radiant_index = radiant_queue.popleft()
            dire_index = dire_queue.popleft()
            
            # The senator with the lower index gets to ban the other senator
            if radiant_index < dire_index:
                # Radiant bans Dire, so Radiant goes to the end of the queue
                radiant_queue.append(radiant_index + len(senate))
            else:
                # Dire bans Radiant, so Dire goes to the end of the queue
                dire_queue.append(dire_index + len(senate))
        
        # Determine the winner
        if radiant_queue:
            return "Radiant"
        else:
            return "Dire"
