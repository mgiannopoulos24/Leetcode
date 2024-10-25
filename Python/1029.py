class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort the costs array by the difference in cost to send each person to City A vs City B
        costs.sort(key=lambda x: x[0] - x[1])
        
        total_cost = 0
        n = len(costs) // 2
        
        # Send the first n people to City A
        for i in range(n):
            total_cost += costs[i][0]
        
        # Send the remaining n people to City B
        for i in range(n, 2 * n):
            total_cost += costs[i][1]
        
        return total_cost
