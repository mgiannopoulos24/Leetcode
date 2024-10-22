class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def matches(query: str, pattern: str) -> bool:
            i, j = 0, 0
            while i < len(query):
                if j < len(pattern) and query[i] == pattern[j]:
                    j += 1
                elif query[i].isupper():
                    # If query[i] is uppercase and doesn't match pattern[j], it's a mismatch
                    return False
                # Else we just skip the lowercase character in the query
                i += 1
            # At the end, j should have traversed all of the pattern
            return j == len(pattern)
        
        # Apply the match function for each query
        return [matches(query, pattern) for query in queries]
