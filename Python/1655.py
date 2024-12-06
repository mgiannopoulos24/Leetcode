from collections import Counter

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        # Count frequencies of numbers in nums
        freq = list(Counter(nums).values())
        
        # Sort quantities in descending order for optimization
        quantity.sort(reverse=True)
        
        # Helper function to use backtracking to check all possibilities
        def backtrack(index):
            if index == len(quantity):
                return True
            
            for i in range(len(freq)):
                if freq[i] >= quantity[index]:
                    # Try assigning the current quantity to this frequency
                    freq[i] -= quantity[index]
                    if backtrack(index + 1):
                        return True
                    # Backtrack if this assignment fails
                    freq[i] += quantity[index]
            
            return False
        
        # Start backtracking from the first customer
        return backtrack(0)
