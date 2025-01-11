from typing import List

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def can_place_segment(segment: List[str], word: str) -> bool:
            """Check if the word or its reverse can fit into the segment."""
            n = len(segment)
            m = len(word)
            if n != m:
                return False
            # Check normal orientation
            if all(segment[i] in (' ', word[i]) for i in range(m)):
                return True
            # Check reversed orientation
            if all(segment[i] in (' ', word[-i - 1]) for i in range(m)):
                return True
            return False

        def extract_segments(line: List[str]) -> List[List[str]]:
            """Extract segments (between '#' or boundaries) from a line."""
            segments = []
            current_segment = []
            for char in line:
                if char == '#':
                    if current_segment:
                        segments.append(current_segment)
                        current_segment = []
                else:
                    current_segment.append(char)
            if current_segment:
                segments.append(current_segment)
            return segments

        # Check rows for horizontal placement
        for row in board:
            for segment in extract_segments(row):
                if can_place_segment(segment, word):
                    return True

        # Check columns for vertical placement
        for col in zip(*board):
            for segment in extract_segments(col):
                if can_place_segment(segment, word):
                    return True

        return False
