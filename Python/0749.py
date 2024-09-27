class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions for 4-directional movement

        def bfs(x, y, visited):
            """ Find the connected region using BFS/DFS starting from (x, y) """
            queue = [(x, y)]
            region = [(x, y)]
            frontier = set()
            perimeter = 0
            visited.add((x, y))
            
            while queue:
                i, j = queue.pop(0)
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if isInfected[ni][nj] == 1 and (ni, nj) not in visited:
                            visited.add((ni, nj))
                            queue.append((ni, nj))
                            region.append((ni, nj))
                        elif isInfected[ni][nj] == 0:
                            frontier.add((ni, nj))
                            perimeter += 1
            return region, frontier, perimeter

        total_walls = 0

        while True:
            regions = []
            frontiers = []
            perimeters = []
            visited = set()

            # Step 1: Find all regions and calculate frontiers and perimeters
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        region, frontier, perimeter = bfs(i, j, visited)
                        if frontier:  # Only add regions that have a frontier to infect
                            regions.append(region)
                            frontiers.append(frontier)
                            perimeters.append(perimeter)

            if not regions:
                break  # No more regions to process

            # Step 2: Find the region that threatens the most uncontaminated cells
            most_threatening = max(range(len(frontiers)), key=lambda k: len(frontiers[k]))

            # Step 3: Quarantine the most threatening region
            total_walls += perimeters[most_threatening]
            for i, j in regions[most_threatening]:
                isInfected[i][j] = -1  # Quarantine the region

            # Step 4: Spread the virus from the remaining regions
            for k in range(len(regions)):
                if k != most_threatening:
                    for i, j in frontiers[k]:
                        isInfected[i][j] = 1  # Spread the virus

        return total_walls
