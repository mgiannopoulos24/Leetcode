class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        result = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            
            # Move the left pointer to the right as long as we have at least one 'a', 'b', and 'c'
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                # When we have a valid substring, add all substrings starting from left to right
                result += len(s) - right
                count[s[left]] -= 1
                left += 1
        
        return result
