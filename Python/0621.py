from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        freq = Counter(tasks)
        
        # Find the maximum frequency of any task
        max_freq = max(freq.values())
        
        # Find how many tasks have this maximum frequency
        max_freq_count = sum(1 for count in freq.values() if count == max_freq)
        
        # Calculate the minimum intervals required
        min_intervals = (max_freq - 1) * (n + 1) + max_freq_count
        
        # The minimum intervals required must be at least the number of tasks
        return max(min_intervals, len(tasks))
