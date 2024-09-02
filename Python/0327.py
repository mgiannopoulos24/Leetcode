from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Initialize prefix sums
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        
        def merge_count(start: int, end: int) -> int:
            if end - start <= 1:
                return 0
            
            mid = (start + end) // 2
            count = merge_count(start, mid) + merge_count(mid, end)
            
            # Counting the ranges in a sorted fashion
            j = k = mid
            temp = []
            r = mid
            
            for left in prefix_sums[start:mid]:
                # Count the ranges [k, j) where the sum lies within [lower, upper]
                while k < end and prefix_sums[k] - left < lower:
                    k += 1
                while j < end and prefix_sums[j] - left <= upper:
                    j += 1
                count += j - k
                
                # Merge process
                while r < end and prefix_sums[r] < left:
                    temp.append(prefix_sums[r])
                    r += 1
                temp.append(left)
            
            # Complete the merge by appending any remaining elements
            while r < end:
                temp.append(prefix_sums[r])
                r += 1
            
            # Copy back the merged and sorted subarray into the original array
            prefix_sums[start:start+len(temp)] = temp
            
            return count
        
        return merge_count(0, len(prefix_sums))
