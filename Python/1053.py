class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        
        # If no such element is found, return the array as it is (it's the smallest permutation)
        if i == -1:
            return arr
        
        # Step 2: Find the largest element to the right of arr[i] that is smaller than arr[i]
        j = n - 1
        while j > i and (arr[j] >= arr[i] or arr[j] == arr[j - 1]):
            j -= 1
        
        # Step 3: Swap the elements at indices i and j
        arr[i], arr[j] = arr[j], arr[i]
        
        return arr
