from typing import List, Dict, Tuple

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # Memoization dictionary
        memo: Dict[Tuple[int, ...], int] = {}

        def dfs(current_needs: Tuple[int, ...]) -> int:
            # Check if we've already computed the result for this state
            if current_needs in memo:
                return memo[current_needs]

            # Base case: if all needs are zero, no cost needed
            if all(x == 0 for x in current_needs):
                return 0

            # Calculate the cost if we buy each item directly
            direct_cost = sum(price[i] * current_needs[i] for i in range(len(price)))

            # Initialize minimum cost with the direct cost
            min_cost = direct_cost

            # Try each special offer
            for offer in special:
                offer_cost = offer[-1]
                offer_items = offer[:-1]
                
                # Check if the offer can be applied
                new_needs = list(current_needs)
                valid_offer = True
                for i in range(len(offer_items)):
                    if new_needs[i] < offer_items[i]:
                        valid_offer = False
                        break
                    new_needs[i] -= offer_items[i]
                
                if valid_offer:
                    # Recur to find the minimum cost after applying this offer
                    min_cost = min(min_cost, offer_cost + dfs(tuple(new_needs)))

            # Store the computed result in the memoization dictionary
            memo[current_needs] = min_cost
            return min_cost

        # Start the recursion with the initial needs
        return dfs(tuple(needs))
