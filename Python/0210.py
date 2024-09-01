from typing import List
from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list for the graph
        adj_list = defaultdict(list)
        # Create an in-degree array to keep track of prerequisites count
        in_degree = [0] * numCourses
        
        # Build the graph and in-degree array
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1
        
        # Initialize the queue with nodes having in-degree of 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []
        
        # Process the nodes
        while queue:
            node = queue.popleft()
            result.append(node)
            
            # For each neighbor, reduce the in-degree and add to queue if in-degree becomes 0
            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If the result contains all courses, return it, otherwise return an empty array
        return result if len(result) == numCourses else []

