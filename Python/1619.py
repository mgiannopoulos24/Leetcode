class Solution:
    def trimMean(self, arr: List[int]) -> float:
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Determine how many elements to trim (5% from both ends)
        n = len(arr)
        trim_count = n // 20  # 5% of the length
        
        # Step 3: Trim the array by slicing
        trimmed_arr = arr[trim_count : n - trim_count]
        
        # Step 4: Calculate the mean of the trimmed array
        trimmed_mean = sum(trimmed_arr) / len(trimmed_arr)
        
        # Step 5: Return the result
        return trimmed_mean
