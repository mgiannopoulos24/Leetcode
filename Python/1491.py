class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        
        total_sum = sum(salary)
        total_sum -= min_salary + max_salary
        
        return total_sum / (len(salary) - 2)
