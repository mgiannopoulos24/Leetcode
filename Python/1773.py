from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # Map ruleKey to the corresponding index in items' structure
        key_to_index = {"type": 0, "color": 1, "name": 2}
        index = key_to_index[ruleKey]
        
        # Count items that match the rule
        count = 0
        for item in items:
            if item[index] == ruleValue:
                count += 1
                
        return count
