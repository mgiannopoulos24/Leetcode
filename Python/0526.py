class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(index: int, used: int) -> int:
            if index > n:
                return 1  # We have formed a valid arrangement
            
            count = 0
            for num in range(1, n + 1):
                # Check if num is not used and satisfies the condition
                if not (used & (1 << (num - 1))):
                    if num % index == 0 or index % num == 0:
                        # Mark num as used and recurse to the next index
                        count += backtrack(index + 1, used | (1 << (num - 1)))
            return count
        
        return backtrack(1, 0)  # Start from index 1 with no numbers used
