class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (n + m)
        sum_of_m_rolls = sum(rolls)
        sum_of_n_rolls = total_sum - sum_of_m_rolls
        
        # Check if the sum for the missing n rolls is achievable
        if sum_of_n_rolls < n or sum_of_n_rolls > 6 * n:
            return []
        
        # Create a list to store the result
        result = [sum_of_n_rolls // n] * n
        remainder = sum_of_n_rolls % n
        
        # Distribute the remainder over the first few elements to ensure the sum is correct
        for i in range(remainder):
            result[i] += 1
        
        return result
