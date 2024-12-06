class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Count the total number of '1's
        total_ones = s.count('1')
        
        # Step 2: If the total number of '1's is not divisible by 3, return 0
        if total_ones % 3 != 0:
            return 0
        
        # Step 3: If the string has no '1's, count how many ways we can split the string
        if total_ones == 0:
            n = len(s)
            # The number of ways to choose 2 split points out of (n - 1) possible locations
            return (n - 1) * (n - 2) // 2 % MOD
        
        # Step 4: We need to split the '1's into 3 equal parts
        ones_per_part = total_ones // 3
        first_split_ways = second_split_ways = 0
        
        # Step 5: Traverse the string and count the valid ways to split
        one_count = 0
        for i, char in enumerate(s):
            if char == '1':
                one_count += 1
            
            # When we reach exactly 'ones_per_part' ones, start counting first split positions
            if one_count == ones_per_part:
                first_split_ways += 1
            # When we reach exactly '2 * ones_per_part' ones, start counting second split positions
            elif one_count == 2 * ones_per_part:
                second_split_ways += 1
        
        # The result is the product of the number of valid split positions between each part
        return (first_split_ways * second_split_ways) % MOD
