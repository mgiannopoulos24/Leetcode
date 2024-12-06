class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # Initialize permutation P = [1, 2, ..., m]
        P = list(range(1, m + 1))
        result = []
        
        # Process each query
        for query in queries:
            # Find the index of query in P
            index = P.index(query)
            # Append the index to the result
            result.append(index)
            # Move the query element to the beginning of P
            P.insert(0, P.pop(index))
        
        return result