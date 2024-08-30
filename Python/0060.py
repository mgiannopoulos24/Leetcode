class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Calculate factorial values
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
        
        # Convert k to zero-based index
        k -= 1
        
        # Initialize the list of numbers and result string
        numbers = list(range(1, n + 1))
        result = []
        
        # Build the permutation
        for i in range(n, 0, -1):
            # Determine the current factorial
            fact = factorials[i - 1]
            
            # Find the index of the current position
            index = k // fact
            result.append(str(numbers[index]))
            
            # Remove the used number from the list
            numbers.pop(index)
            
            # Update k
            k %= fact
        
        return ''.join(result)
