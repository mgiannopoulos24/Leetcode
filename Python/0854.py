from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        # Helper function to swap characters in a string
        def swap(s, i, j):
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            return ''.join(s_list)
        
        # Early exit if the strings are already equal
        if s1 == s2:
            return 0
        
        # BFS initialization
        queue = deque([(s1, 0)])  # (current string, current swap count)
        visited = set([s1])
        
        while queue:
            current, swaps = queue.popleft()
            
            # Iterate through each possible swap
            for i in range(len(current)):
                if current[i] != s2[i]:  # Only consider swapping if not in place
                    for j in range(i + 1, len(current)):
                        if current[j] == s2[i]:  # Find a matching character to swap with
                            # Generate the new state by swapping
                            new_state = swap(current, i, j)
                            if new_state == s2:
                                return swaps + 1
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append((new_state, swaps + 1))
                    break  # Swap with the first mismatching position
        
        return -1  # This line should not be reached as s2 is an anagram of s1

