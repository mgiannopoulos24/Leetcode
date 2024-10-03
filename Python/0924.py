from typing import List, Set
from collections import defaultdict, deque

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def bfs(start: int) -> Set[int]:
            queue = deque([start])
            visited = set([start])
            while queue:
                node = queue.popleft()
                for neighbor in range(n):
                    if graph[node][neighbor] == 1 and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return visited
        
        n = len(graph)
        initial.sort()
        
        # Step 1: Find all components
        components = []
        visited_global = set()
        for i in range(n):
            if i not in visited_global:
                component = bfs(i)
                components.append(component)
                visited_global.update(component)
        
        # Step 2: Determine component each initial node belongs to
        node_to_component = {}
        component_to_initial_nodes = defaultdict(set)
        
        for component in components:
            for node in component:
                node_to_component[node] = component
                if node in initial:
                    component_to_initial_nodes[frozenset(component)].add(node)
        
        # Step 3: Evaluate the impact of removing each node in initial
        min_infected_nodes = float('inf')
        result_node = float('inf')
        
        for node in initial:
            affected_components = defaultdict(int)
            total_infected_nodes = 0
            
            for component in components:
                component_frozen = frozenset(component)
                if node in component:
                    # If removing the node, check if the component still has malware spread
                    initial_nodes_in_component = component_to_initial_nodes[component_frozen] - {node}
                    if initial_nodes_in_component:
                        total_infected_nodes += len(component)
                else:
                    if component_to_initial_nodes[component_frozen]:
                        total_infected_nodes += len(component)
            
            # Update the minimum infected nodes and result node
            if total_infected_nodes < min_infected_nodes:
                min_infected_nodes = total_infected_nodes
                result_node = node
            elif total_infected_nodes == min_infected_nodes:
                result_node = min(result_node, node)
        
        return result_node