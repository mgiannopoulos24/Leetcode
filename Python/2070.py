from bisect import bisect_right

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items based on price
        items.sort()
        
        # Precompute the maximum beauty up to each index
        max_beauty = []
        current_max = 0
        for price, beauty in items:
            current_max = max(current_max, beauty)
            max_beauty.append(current_max)
        
        # Prepare the result for each query
        result = []
        for q in queries:
            # Find the rightmost index where price is <= q
            idx = bisect_right([item[0] for item in items], q) - 1
            if idx >= 0:
                result.append(max_beauty[idx])
            else:
                result.append(0)
        
        return result