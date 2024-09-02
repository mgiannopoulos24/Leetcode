from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort the people list:
        # - Sort by height in descending order
        # - For people with the same height, sort by k in ascending order
        people.sort(key=lambda x: (-x[0], x[1]))
        
        # Initialize an empty queue
        queue = []
        
        # Insert each person into the queue
        for person in people:
            height, k = person
            # Insert the person at index k
            queue.insert(k, person)
        
        return queue
