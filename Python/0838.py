class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        
        # Step 1: Compute forces from the right ('R')
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # Set force to max (we use `n` as the max to ensure it overrides any left forces)
            elif dominoes[i] == 'L':
                force = 0  # No force from right after a left push
            else:
                force = max(force - 1, 0)  # Gradually decrease the force
            forces[i] += force
        
        # Step 2: Compute forces from the left ('L')
        force = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                force = n  # Set force to max (we use `n` as the max to ensure it overrides any right forces)
            elif dominoes[i] == 'R':
                force = 0  # No force from left after a right push
            else:
                force = max(force - 1, 0)  # Gradually decrease the force
            forces[i] -= force
        
        # Step 3: Compute the result based on the net forces
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')
        
        return ''.join(result)
