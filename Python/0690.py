# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        # Step 1: Create a mapping from ID to Employee
        employee_map = {employee.id: employee for employee in employees}
        
        # Step 2: Perform DFS to calculate the total importance
        def dfs(emp_id: int) -> int:
            employee = employee_map[emp_id]
            # Start with the current employee's importance
            total_importance = employee.importance
            # Recursively add the importance of all subordinates
            for sub_id in employee.subordinates:
                total_importance += dfs(sub_id)
            return total_importance
        
        # Start DFS from the given employee ID
        return dfs(id)
