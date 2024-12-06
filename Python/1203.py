from typing import List
from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        """
        Sorts the items based on group dependencies and item dependencies.

        Args:
        n (int): Number of items.
        m (int): Number of groups.
        group (List[int]): List indicating the group of each item.
        beforeItems (List[List[int]]): List of dependencies for each item.

        Returns:
        List[int]: Sorted list of items satisfying the constraints, or an empty list if impossible.
        """

        # Step 1: Assign unique group IDs to items with group[i] == -1
        # Assign new group IDs starting from m
        new_group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group_id
                new_group_id += 1
        total_groups = new_group_id  # Total number of groups after assignment

        # Step 2: Build Group Dependency Graph
        group_graph = defaultdict(list)  # Adjacency list for groups
        group_indegree = [0] * total_groups  # Indegree for groups

        # Step 3: Build Item Dependency Graph
        item_graph = defaultdict(list)  # Adjacency list for items
        item_indegree = [0] * n  # Indegree for items

        for curr_item in range(n):
            for pre_item in beforeItems[curr_item]:
                # Add edge pre_item -> curr_item
                item_graph[pre_item].append(curr_item)
                item_indegree[curr_item] += 1

                # If items belong to different groups, add dependency between groups
                if group[pre_item] != group[curr_item]:
                    group_graph[group[pre_item]].append(group[curr_item])
                    group_indegree[group[curr_item]] += 1

        # Step 4: Perform Topological Sort on Groups
        group_order = self.topologicalSort(total_groups, group_graph, group_indegree)
        if not group_order:
            return []  # Cycle detected in group dependencies

        # Step 5: Organize items by their groups
        group_to_items = defaultdict(list)
        for item in range(n):
            group_to_items[group[item]].append(item)

        # Step 6: Perform Topological Sort on Items
        item_order = self.topologicalSort(n, item_graph, item_indegree)
        if not item_order:
            return []  # Cycle detected in item dependencies

        # Step 7: Arrange items within their groups based on item_order
        item_position = {item: idx for idx, item in enumerate(item_order)}
        for grp in group_to_items:
            group_to_items[grp].sort(key=lambda x: item_position[x])

        # Step 8: Combine items based on group_order
        result = []
        for grp in group_order:
            result.extend(group_to_items[grp])

        return result

    def topologicalSort(self, total_nodes: int, graph: defaultdict, indegree: List[int]) -> List[int]:
        """
        Performs topological sorting on a graph.

        Args:
        total_nodes (int): Total number of nodes in the graph.
        graph (defaultdict): Adjacency list representing the graph.
        indegree (List[int]): List of indegrees for each node.

        Returns:
        List[int]: Topologically sorted list of nodes, or empty list if cycle detected.
        """
        queue = deque()
        for node in range(total_nodes):
            if indegree[node] == 0:
                queue.append(node)

        sorted_order = []
        while queue:
            node = queue.popleft()
            sorted_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(sorted_order) == total_nodes:
            return sorted_order
        else:
            return []  # Cycle detected