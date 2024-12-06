class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Step 1: Count the soldiers in each row
        soldier_counts = []
        for i, row in enumerate(mat):
            count = sum(row)  # Count the number of 1's (soldiers) in the row
            soldier_counts.append((count, i))  # Store as (count, index)
        
        # Step 2: Sort the rows first by soldier count, then by row index
        soldier_counts.sort()
        
        # Step 3: Extract the first k indices from the sorted list
        return [index for _, index in soldier_counts[:k]]
