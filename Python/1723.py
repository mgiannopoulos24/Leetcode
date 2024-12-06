from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # Sort jobs in descending order to optimize backtracking by assigning larger jobs first
        jobs.sort(reverse=True)

        # Binary search range
        left, right = max(jobs), sum(jobs)
        
        def canDistribute(maxTime):
            # Backtracking function to check if distribution is possible under maxTime
            workloads = [0] * k
            
            def backtrack(index):
                if index == len(jobs):
                    return True
                job = jobs[index]
                for i in range(k):
                    if workloads[i] + job <= maxTime:
                        workloads[i] += job
                        if backtrack(index + 1):
                            return True
                        workloads[i] -= job
                    if workloads[i] == 0:
                        break
                return False
            
            return backtrack(0)
        
        # Binary search on the minimum maximum time
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
