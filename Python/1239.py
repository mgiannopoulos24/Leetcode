class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Helper function to check if a string has all unique characters
        def is_unique(s: str) -> bool:
            return len(s) == len(set(s))
        
        # Backtracking function
        def backtrack(index: int, current: str) -> int:
            # If the current string is not unique, return 0
            if not is_unique(current):
                return 0
            
            # Initialize max_length with the length of the current unique string
            max_length = len(current)
            
            # Try to add more strings from the remaining elements in arr
            for i in range(index, len(arr)):
                max_length = max(max_length, backtrack(i + 1, current + arr[i]))
            
            return max_length
        
        # Start the backtracking from the first string
        return backtrack(0, "")
