from collections import defaultdict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Step 1: Count the occurrences of each string in the array
        count = defaultdict(int)
        for s in arr:
            count[s] += 1
        
        # Step 2: Identify distinct strings (those with count == 1)
        distinct = []
        for s in arr:
            if count[s] == 1:
                distinct.append(s)
        
        # Step 3: Return the kth distinct string if it exists
        if len(distinct) >= k:
            return distinct[k - 1]
        else:
            return ""