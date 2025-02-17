from bisect import bisect_right

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items based on price
        items.sort()
        
        # Precompute the maximum beauty up to each index in-place
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i-1][1])
        
        # Extract the sorted prices for binary search
        prices = [item[0] for item in items]
        
        # Prepare the result for each query
        result = []
        for q in queries:
            # Find the rightmost index where price is <= q
            idx = bisect_right(prices, q) - 1
            if idx >= 0:
                result.append(items[idx][1])
            else:
                result.append(0)
        
        return result