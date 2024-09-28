class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Step 1: Zip the indices, sources, and targets together and sort by indices in reverse order
        operations = sorted(zip(indices, sources, targets), reverse=True)
        
        # Step 2: Perform the replacements
        for index, source, target in operations:
            # Check if the substring matches at the given index
            if s[index:index+len(source)] == source:
                # Replace the substring in s
                s = s[:index] + target + s[index+len(source):]
        
        return s
