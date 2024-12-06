from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0  # If the array has only one element, we're already at the last index.
        
        n = len(arr)
        graph = defaultdict(list)
        
        # Step 1: Build a graph where each value in arr points to all its indices
        for i in range(n):
            graph[arr[i]].append(i)
        
        # Step 2: BFS initialization
        queue = deque([(0, 0)])  # (index, steps)
        visited = set([0])
        
        # Step 3: BFS traversal
        while queue:
            index, steps = queue.popleft()
            
            # If we've reached the last index, return the number of steps
            if index == n - 1:
                return steps
            
            # Check neighbors: i - 1 and i + 1
            for next_index in [index - 1, index + 1]:
                if 0 <= next_index < n and next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, steps + 1))
            
            # Check all indices with the same value as arr[index]
            for next_index in graph[arr[index]]:
                if next_index != index and next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, steps + 1))
            
            # Once we've used all indices with the same value, clear them to avoid redundant checks
            graph[arr[index]].clear()
        
        return -1  # In case we never reach the last index (though the problem guarantees we can)
