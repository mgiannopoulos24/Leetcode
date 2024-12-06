from bisect import bisect_right
from math import comb
from collections import defaultdict

class Solution:
    def gcdValues(self, nums, queries):
        max_num = max(nums)
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] +=1

        cnt_gcd = [0]*(max_num + 1)
        total_pairs = [0]*(max_num +1)

        # Compute count of numbers divisible by each gcd value
        for gcd_value in range(1, max_num+1):
            cnt = 0
            for multiple in range(gcd_value, max_num+1, gcd_value):
                cnt += freq[multiple]
            cnt_gcd[gcd_value] = cnt

        # Compute total pairs for each gcd_value
        for gcd_value in range(max_num, 0, -1):
            cnt = cnt_gcd[gcd_value]
            if cnt >=2:
                total_pairs[gcd_value] = cnt * (cnt -1) //2
            else:
                total_pairs[gcd_value] =0

            # Subtract counts of multiples to avoid overcounting
            for multiple in range(2*gcd_value, max_num+1, gcd_value):
                total_pairs[gcd_value] -= total_pairs[multiple]

        # Collect gcd_values with positive pair counts
        gcd_list = []
        counts = []
        for gcd_value in range(1, max_num+1):
            if total_pairs[gcd_value] >0:
                gcd_list.append(gcd_value)
                counts.append(total_pairs[gcd_value])

        # Sort gcd_values and compute cumulative counts
        sorted_gcd_list = gcd_list  # Already in order since we processed from 1 to max_num
        cumulative_counts = []
        cum_sum = 0
        for count in counts:
            cum_sum += count
            cumulative_counts.append(cum_sum)

        # Answer the queries
        result = []
        for q in queries:
            idx = bisect_right(cumulative_counts, q)
            result.append(sorted_gcd_list[idx])

        return result
