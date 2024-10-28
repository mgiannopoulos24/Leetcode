class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # Step 1: Count the zeros in the array to determine how much shifting is needed
        zeros = arr.count(0)
        n = len(arr)
        
        # Step 2: Traverse the array from the end and shift elements accordingly
        for i in range(n - 1, -1, -1):
            # If this index would be within the new bounds after accounting for the zeros
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            
            # If the current element is zero, we need to "duplicate" it
            if arr[i] == 0:
                zeros -= 1  # Use up one of the extra spaces for the duplicated zero
                if i + zeros < n:
                    arr[i + zeros] = 0
