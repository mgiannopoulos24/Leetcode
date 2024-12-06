import heapq

class Solution:
    def kthSmallest(self, mat, k):
        m = len(mat)
        n = len(mat[0])
        
        # Initialize prev with the first row
        prev = mat[0][:]  # Make a copy to avoid modifying the original row
        prev.sort()
        prev = prev[:k]  # Keep only up to k elements

        for i in range(1, m):
            # Merge prev and mat[i]
            curr = mat[i][:]
            curr.sort()
            curr = curr[:k]  # Keep only up to k elements
            prev = self.merge(prev, curr, k)
        
        # Return the k-th smallest sum
        if len(prev) >= k:
            return prev[k-1]
        else:
            return prev[-1]

    def merge(self, A, B, k):
        import heapq
        heap = []
        visited = set()
        result = []
        heapq.heappush(heap, (A[0]+B[0], 0, 0))
        visited.add((0, 0))
        while len(result) < k and heap:
            sum_ab, i, j = heapq.heappop(heap)
            result.append(sum_ab)
            if i+1 < len(A) and (i+1, j) not in visited:
                heapq.heappush(heap, (A[i+1]+B[j], i+1, j))
                visited.add((i+1, j))
            if j+1 < len(B) and (i, j+1) not in visited:
                heapq.heappush(heap, (A[i]+B[j+1], i, j+1))
                visited.add((i, j+1))
        return result
