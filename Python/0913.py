from functools import lru_cache
from typing import List

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        # Constants to represent players and outcomes
        MOUSE_TURN = 0
        CAT_TURN = 1
        MOUSE_WIN = 1
        CAT_WIN = 2
        DRAW = 0
        MAX_TURNS = 200  # Increased to handle deeper game states

        n = len(graph)
        
        @lru_cache(maxsize=None)
        def dfs(mouse: int, cat: int, turn: int, depth: int) -> int:
            # Base Cases
            if mouse == 0:
                return MOUSE_WIN
            if mouse == cat:
                return CAT_WIN
            if depth > MAX_TURNS:
                return DRAW  # Assume draw if exceeding max depth

            if turn == MOUSE_TURN:
                # Mouse's turn: Try to maximize its chance to win
                outcome = CAT_WIN  # Initialize as worst case: Cat wins
                for next_mouse in graph[mouse]:
                    result = dfs(next_mouse, cat, CAT_TURN, depth + 1)
                    if result == MOUSE_WIN:
                        return MOUSE_WIN  # Mouse can force a win
                    elif result == DRAW:
                        outcome = DRAW  # Mouse can at least draw
                return outcome
            else:
                # Cat's turn: Try to maximize its chance to win
                outcome = MOUSE_WIN  # Initialize as worst case: Mouse wins
                for next_cat in graph[cat]:
                    if next_cat == 0:
                        continue  # Cat cannot move to the hole
                    result = dfs(mouse, next_cat, MOUSE_TURN, depth + 1)
                    if result == CAT_WIN:
                        return CAT_WIN  # Cat can force a win
                    elif result == DRAW:
                        outcome = DRAW  # Cat can at least draw
                return outcome

        # Start the game: Mouse at node 1, Cat at node 2, Mouse's turn, depth 0
        return dfs(1, 2, MOUSE_TURN, 0)
