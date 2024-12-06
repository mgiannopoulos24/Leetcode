class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # Step 1: Create a dictionary that maps the first element of each piece to the piece
        piece_dict = {p[0]: p for p in pieces}
        
        # Step 2: Traverse the arr and try to match with the pieces
        i = 0
        while i < len(arr):
            # Step 3: Check if arr[i] is the first element of any piece
            if arr[i] not in piece_dict:
                return False
            
            # Get the corresponding piece
            piece = piece_dict[arr[i]]
            
            # Step 4: Check if arr from i matches the piece
            if arr[i:i + len(piece)] != piece:
                return False
            
            # Step 5: Move the index forward by the length of the matched piece
            i += len(piece)
        
        # If the whole arr matches, return True
        return True
