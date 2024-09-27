class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Set of prime numbers up to 20 (the max set bits count we care about)
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19}
        
        # Function to count the number of set bits
        def count_set_bits(x):
            return bin(x).count('1')
        
        # Initialize the result count
        count = 0
        
        # Iterate through the range [left, right]
        for num in range(left, right + 1):
            # Count set bits
            set_bits = count_set_bits(num)
            # Check if the number of set bits is a prime number
            if set_bits in prime_set:
                count += 1
        
        return count
