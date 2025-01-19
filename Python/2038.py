class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # Initialize counters for Alice and Bob's moves
        alice_moves = 0
        bob_moves = 0
        
        # Traverse the string to count valid moves
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    alice_moves += 1
                elif colors[i] == 'B':
                    bob_moves += 1
        
        # Alice wins if she has more moves than Bob
        return alice_moves > bob_moves