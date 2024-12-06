from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Build the tree structure
        subordinates = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                subordinates[manager[i]].append(i)
        
        # DFS to calculate the total time
        def dfs(employee_id):
            # If this employee has no subordinates, return 0
            if not subordinates[employee_id]:
                return 0
            # Compute the max time taken by any of the subordinates
            max_time = 0
            for subordinate in subordinates[employee_id]:
                max_time = max(max_time, dfs(subordinate))
            # Return the inform time for this employee + the maximum time needed for subordinates
            return informTime[employee_id] + max_time
        
        # Start DFS from the head of the company
        return dfs(headID)
