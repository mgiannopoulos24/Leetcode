class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Step 1: Sort the folders lexicographically
        folder.sort()
        
        result = []
        prev_folder = ""
        
        # Step 2: Iterate through each folder
        for f in folder:
            # Step 3: If current folder is not a subfolder of the previous folder, add it to the result
            if not prev_folder or not f.startswith(prev_folder + '/'):
                result.append(f)
                prev_folder = f  # Update the previous folder
        
        return result
