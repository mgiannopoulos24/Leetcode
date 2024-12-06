class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_count = {}
        result = []
        
        for name in names:
            if name not in name_count:
                # Unique name, use as is
                result.append(name)
                name_count[name] = 1  # Mark it as used
            else:
                # Name already exists, find the smallest valid suffix
                k = name_count[name]
                while f"{name}({k})" in name_count:
                    k += 1
                new_name = f"{name}({k})"
                result.append(new_name)
                
                # Update the dictionaries for future references
                name_count[name] = k + 1  # Increment base name count
                name_count[new_name] = 1  # Mark the new name as used
        
        return result
