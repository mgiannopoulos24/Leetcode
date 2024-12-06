class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort tasks by the difference (minimum - actual) in descending order
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        # Helper function to check if we can complete all tasks with given initial energy
        def canComplete(initial_energy):
            current_energy = initial_energy
            for actual, minimum in tasks:
                if current_energy < minimum:
                    return False
                current_energy -= actual
            return True
        
        # Binary search to find the minimum initial energy required
        low, high = sum([task[0] for task in tasks]), sum([task[1] for task in tasks])
        
        while low < high:
            mid = (low + high) // 2
            if canComplete(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
