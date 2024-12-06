from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Step 1: Count the frequency of each element
        freq = Counter(arr)
        
        # Step 2: Sort frequencies in descending order
        frequencies = sorted(freq.values(), reverse=True)
        
        # Step 3: Remove elements with the highest frequencies until at least half of the array is removed
        total_removed = 0
        target = len(arr) // 2
        set_size = 0
        
        for count in frequencies:
            total_removed += count
            set_size += 1
            if total_removed >= target:
                break
        
        # Step 4: Return the number of elements removed
        return set_size
