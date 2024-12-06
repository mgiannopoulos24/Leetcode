class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_achievable = 0
        total_requests = len(requests)
        
        # Iterate over all subsets of requests using bit masking
        for mask in range(1 << total_requests):
            # Initialize the balance array for each building
            balance = [0] * n
            count = 0  # Count the number of requests in this subset
            
            # Process each request in the subset
            for i in range(total_requests):
                if mask & (1 << i):  # Check if the i-th request is included in the subset
                    from_building, to_building = requests[i]
                    balance[from_building] -= 1  # One employee leaves from from_building
                    balance[to_building] += 1    # One employee enters to_building
                    count += 1
            
            # Check if the balance for all buildings is zero
            if all(b == 0 for b in balance):
                max_achievable = max(max_achievable, count)
        
        return max_achievable
