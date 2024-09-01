from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost = 0, 0
        current_gas, start_index = 0, 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]
            
            if current_gas < 0:
                # If we cannot reach the next station, reset the start_index
                start_index = i + 1
                current_gas = 0
        
        # If the total gas is at least the total cost, return the start_index
        if total_gas >= total_cost:
            return start_index
        else:
            return -1
