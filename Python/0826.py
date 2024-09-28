class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        max_profit_at_difficulty = [0] * (len(jobs))
        max_profit = 0

        # Precompute the maximum profit for each difficulty level
        for i, (d, p) in enumerate(jobs):
            max_profit = max(max_profit, p)
            max_profit_at_difficulty[i] = max_profit

        # Sort workers
        worker.sort()
        
        total_profit = 0
        job_index = 0

        # Compute the maximum profit for each worker
        for ability in worker:
            # Move the job index to the right position
            while job_index < len(jobs) and jobs[job_index][0] <= ability:
                job_index += 1
            # If job_index is not 0, it means there's at least one job that can be performed
            if job_index > 0:
                total_profit += max_profit_at_difficulty[job_index - 1]

        return total_profit
