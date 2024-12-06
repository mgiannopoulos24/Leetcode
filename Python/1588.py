class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)

        # Traverse each element in the array
        for i in range(n):
            # Calculate the number of subarrays that include arr[i]
            # This is derived from counting how many subarrays can start
            # and end in the different positions that contain arr[i]
            start_count = i + 1  # How many subarrays start before or at i
            end_count = n - i    # How many subarrays end after or at i
            # Total subarrays that include arr[i] is start_count * end_count
            total_subarrays = start_count * end_count

            # Half (or roughly half) of these subarrays are odd-length
            odd_count = (total_subarrays + 1) // 2

            # Add the contribution of arr[i] to the total sum
            total_sum += odd_count * arr[i]
        
        return total_sum
