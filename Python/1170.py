from bisect import bisect_right

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # Helper function to calculate f(s) - the frequency of the smallest lexicographical character
        def f(s: str) -> int:
            smallest_char = min(s)
            return s.count(smallest_char)
        
        # Step 1: Calculate f(word) for each word in words
        word_frequencies = [f(word) for word in words]
        # Step 2: Sort the word frequencies for binary search usage
        word_frequencies.sort()
        
        result = []
        
        # Step 3: For each query, calculate f(query)
        for query in queries:
            query_freq = f(query)
            # Step 4: Use binary search to find how many word frequencies are greater than query_freq
            # bisect_right gives us the index where query_freq would fit in the sorted list,
            # so all elements to the right of this index are greater than query_freq.
            count_greater = len(word_frequencies) - bisect_right(word_frequencies, query_freq)
            result.append(count_greater)
        
        return result
