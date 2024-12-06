from typing import List
import collections

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        # Flatten the matrix and sort the elements with their positions
        vals = []
        for i in range(m):
            for j in range(n):
                vals.append((matrix[i][j], i, j))
        vals.sort()

        answer = [[0]*n for _ in range(m)]
        rowMaxRank = [0]*m
        colMaxRank = [0]*n

        parent = {}
        rank = {}

        def find(u):
            parent.setdefault(u, u)
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv

        prev_val = None
        positions = []

        for idx in range(len(vals) + 1):
            if idx < len(vals):
                value, i, j = vals[idx]
                if value != prev_val and positions:
                    # Process positions with value prev_val
                    # Initialize Union-Find
                    parent = {}
                    # Build positions_in_row and positions_in_col
                    positions_in_row = collections.defaultdict(list)
                    positions_in_col = collections.defaultdict(list)
                    for x, y in positions:
                        positions_in_row[x].append((x, y))
                        positions_in_col[y].append((x, y))

                    # Union positions in the same row and column
                    for row_positions in positions_in_row.values():
                        base = row_positions[0]
                        for pos in row_positions[1:]:
                            union(base, pos)
                    for col_positions in positions_in_col.values():
                        base = col_positions[0]
                        for pos in col_positions[1:]:
                            union(base, pos)

                    # Build root to positions mapping
                    root_to_positions = collections.defaultdict(list)
                    for x, y in positions:
                        root = find((x, y))
                        root_to_positions[root].append((x, y))

                    # Assign ranks
                    for root, pos_list in root_to_positions.items():
                        max_rank = 0
                        for x, y in pos_list:
                            max_rank = max(max_rank, rowMaxRank[x], colMaxRank[y])
                        rank_val = max_rank + 1
                        for x, y in pos_list:
                            answer[x][y] = rank_val
                            rowMaxRank[x] = rank_val
                            colMaxRank[y] = rank_val

                    positions = []

                prev_val = value
                positions.append((i, j))
            else:
                if positions:
                    # Process the last group
                    parent = {}
                    positions_in_row = collections.defaultdict(list)
                    positions_in_col = collections.defaultdict(list)
                    for x, y in positions:
                        positions_in_row[x].append((x, y))
                        positions_in_col[y].append((x, y))

                    for row_positions in positions_in_row.values():
                        base = row_positions[0]
                        for pos in row_positions[1:]:
                            union(base, pos)
                    for col_positions in positions_in_col.values():
                        base = col_positions[0]
                        for pos in col_positions[1:]:
                            union(base, pos)

                    root_to_positions = collections.defaultdict(list)
                    for x, y in positions:
                        root = find((x, y))
                        root_to_positions[root].append((x, y))

                    for root, pos_list in root_to_positions.items():
                        max_rank = 0
                        for x, y in pos_list:
                            max_rank = max(max_rank, rowMaxRank[x], colMaxRank[y])
                        rank_val = max_rank + 1
                        for x, y in pos_list:
                            answer[x][y] = rank_val
                            rowMaxRank[x] = rank_val
                            colMaxRank[y] = rank_val

        return answer
