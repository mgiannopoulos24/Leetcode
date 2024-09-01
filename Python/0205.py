class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Hash maps to store character mappings
        s_to_t = {}
        t_to_s = {}
        
        # Iterate over characters in both strings
        for c_s, c_t in zip(s, t):
            # Check if there is an existing mapping in s_to_t
            if c_s in s_to_t:
                if s_to_t[c_s] != c_t:
                    return False
            else:
                s_to_t[c_s] = c_t
            
            # Check if there is an existing mapping in t_to_s
            if c_t in t_to_s:
                if t_to_s[c_t] != c_s:
                    return False
            else:
                t_to_s[c_t] = c_s
                
        return True
