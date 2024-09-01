from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize in-degree array and adjacency list
        in_degree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        
        # Fill the in-degree array and adjacency list
        for dest, src in prerequisites:
            in_degree[dest] += 1
            adj_list[src].append(dest)
        
        # Initialize the queue with courses having no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        courses_processed = 0
        
        # Process the courses
        while queue:
            course = queue.popleft()
            courses_processed += 1
            
            # Reduce the in-degree of each neighbor
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                # If in-degree becomes zero, add to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If all courses are processed, return True, otherwise False
        return courses_processed == numCourses
