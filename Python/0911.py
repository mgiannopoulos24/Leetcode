from collections import defaultdict
from bisect import bisect_right

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        vote_count = defaultdict(int)
        current_leader = -1
        
        # Traverse through the persons and times to compute leaders at each time
        for i, person in enumerate(persons):
            vote_count[person] += 1
            
            # If the current person has more votes than the current leader, or there is a tie but
            # the current person was the most recent, update the leader.
            if current_leader == -1 or vote_count[person] >= vote_count[current_leader]:
                current_leader = person
            
            # Append the leader at this time
            self.leaders.append(current_leader)

    def q(self, t: int) -> int:
        # Use binary search to find the latest time that is <= t
        idx = bisect_right(self.times, t) - 1
        return self.leaders[idx]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)