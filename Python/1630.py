class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        
        # Iterate through each query range
        for i in range(len(l)):
            # Extract the subarray from nums[l[i] to r[i]]
            subarray = nums[l[i]:r[i] + 1]
            
            # Sort the subarray
            subarray.sort()
            
            # Check if the sorted subarray forms an arithmetic sequence
            is_arithmetic = True
            difference = subarray[1] - subarray[0]
            for j in range(2, len(subarray)):
                if subarray[j] - subarray[j - 1] != difference:
                    is_arithmetic = False
                    break
            
            # Append the result
            result.append(is_arithmetic)
        
        return result
