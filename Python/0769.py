class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Initialize
        chunks = 0
        max_in_chunk = 0
        
        # Traverse the array
        for i in range(len(arr)):
            # Update the maximum value in the current chunk
            max_in_chunk = max(max_in_chunk, arr[i])
            
            # Check if we can end a chunk at this index
            if max_in_chunk == i:
                chunks += 1
        
        return chunks
