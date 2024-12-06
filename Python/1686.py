class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        
        # Step 1: Create a list of tuples where each tuple is (combined_value, alice_value, bob_value)
        stones = []
        for i in range(n):
            combined_value = aliceValues[i] + bobValues[i]
            stones.append((combined_value, aliceValues[i], bobValues[i]))
        
        # Step 2: Sort the stones by combined_value in descending order
        stones.sort(reverse=True, key=lambda x: x[0])
        
        # Step 3: Simulate the game
        alice_score = 0
        bob_score = 0
        
        for turn in range(n):
            combined_value, alice_value, bob_value = stones[turn]
            if turn % 2 == 0:
                # Alice's turn (even index)
                alice_score += alice_value
            else:
                # Bob's turn (odd index)
                bob_score += bob_value
        
        # Step 4: Compare the final scores
        if alice_score > bob_score:
            return 1
        elif bob_score > alice_score:
            return -1
        else:
            return 0
