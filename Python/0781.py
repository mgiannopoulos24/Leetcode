from typing import List
from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Count the frequency of each answer
        answer_count = Counter(answers)
        
        total_rabbits = 0
        
        for answer, count in answer_count.items():
            group_size = answer + 1
            # Calculate the number of groups required for this answer
            num_groups = (count + group_size - 1) // group_size
            total_rabbits += num_groups * group_size
        
        return total_rabbits
