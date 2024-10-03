from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Count frequency of each number in arr
        count = Counter(arr)
        nums = sorted(count.keys())  # Unique numbers in arr, sorted
        
        result = 0
        
        # Step 2: Iterate through each pair of numbers
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                x, y = nums[i], nums[j]
                z = target - (x + y)
                
                # Check if z is a valid number and exists in the count
                if z in count and z >= y:  # Ensure z is at least as large as y to avoid duplication
                    if x == y == z:
                        # Case 1: x == y == z
                        result += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                    elif x == y != z:
                        # Case 2: x == y != z
                        result += count[x] * (count[x] - 1) // 2 * count[z]
                    elif x != y and y == z:
                        # Case 3: x != y == z
                        result += count[x] * count[y] * (count[y] - 1) // 2
                    elif x != y and y != z:
                        # Case 4: x != y != z
                        result += count[x] * count[y] * count[z]
                    
        return result % MOD
