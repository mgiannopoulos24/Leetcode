from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # The initial super ugly number is 1
        ugly_numbers = [1]
        # Initialize a min-heap
        heap = []
        
        # Add the initial primes into the heap
        for prime in primes:
            heapq.heappush(heap, (prime, prime, 0))  # (next_value, prime, index_in_ugly_numbers)

        while len(ugly_numbers) < n:
            # Pop the smallest element from the heap
            next_ugly, prime, index = heapq.heappop(heap)
            # Only add this new number if it's different from the last added to ugly_numbers
            if next_ugly != ugly_numbers[-1]:
                ugly_numbers.append(next_ugly)
            # Push the next value derived from this prime
            heapq.heappush(heap, (prime * ugly_numbers[index + 1], prime, index + 1))
        
        return ugly_numbers[-1]