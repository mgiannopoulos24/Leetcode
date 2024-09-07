from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # Dictionary to map content to list of file paths
        content_to_paths = {}
        
        for path in paths:
            # Split the path by spaces, the first part is the directory
            parts = path.split(' ')
            directory = parts[0]
            
            # Remaining parts are files with content
            for file in parts[1:]:
                # Split file name and its content
                file_name, file_content = file.split('(')
                file_content = file_content[:-1]  # Remove the closing parenthesis
                
                # Full path to the file
                full_path = f"{directory}/{file_name}"
                
                # Group by content
                if file_content not in content_to_paths:
                    content_to_paths[file_content] = []
                content_to_paths[file_content].append(full_path)
        
        # Filter out groups of files that have duplicate content
        result = [group for group in content_to_paths.values() if len(group) > 1]
        
        return result
