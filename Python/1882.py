class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        import heapq

        free_servers = [(w, i) for i, w in enumerate(servers)]  # (weight, index)
        busy_servers = []  # (time_free, weight, index)
        heapq.heapify(free_servers)

        ans = []
        time = 0

        for j, task in enumerate(tasks):
            time = max(time, j)

            # Free up servers that have finished tasks
            while busy_servers and busy_servers[0][0] <= time:
                _, w, i = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (w, i))

            # If no free servers, fast-forward time
            if not free_servers:
                time = busy_servers[0][0]
                while busy_servers and busy_servers[0][0] <= time:
                    _, w, i = heapq.heappop(busy_servers)
                    heapq.heappush(free_servers, (w, i))

            # Assign the task
            w, i = heapq.heappop(free_servers)
            ans.append(i)
            heapq.heappush(busy_servers, (time + task, w, i))

        return ans
