class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove dashes and convert to uppercase
        cleaned_string = s.replace('-', '').upper()
        
        # Calculate the length of the first group
        first_group_length = len(cleaned_string) % k
        if first_group_length == 0 and len(cleaned_string) > 0:
            first_group_length = k
        
        # Start building the result
        result = []
        
        # Append the first group if its length is non-zero
        if first_group_length > 0:
            result.append(cleaned_string[:first_group_length])
        
        # Append the remaining groups of length k
        for i in range(first_group_length, len(cleaned_string), k):
            result.append(cleaned_string[i:i+k])
        
        # Join the result with dashes and return
        return '-'.join(result)

