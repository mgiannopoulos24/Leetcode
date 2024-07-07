from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagrams_map:
                anagrams_map[sorted_s].append(s)
            else:
                anagrams_map[sorted_s] = [s]
        
        return list(anagrams_map.values())
