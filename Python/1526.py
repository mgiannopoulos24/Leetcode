class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = target[0]  # Initial operations to reach the first element
        
        # Traverse the target array and compute the required operations
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
        
        return operations
