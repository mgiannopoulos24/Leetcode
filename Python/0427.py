from typing import List

class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        def isUniform(x1, y1, x2, y2):
            """ Check if the sub-grid from (x1, y1) to (x2, y2) is uniform. """
            value = grid[x1][y1]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if grid[i][j] != value:
                        return False
            return True
        
        def buildQuadTree(x1, y1, x2, y2):
            """ Recursively build the Quad-Tree for the sub-grid. """
            if isUniform(x1, y1, x2, y2):
                return Node(val=grid[x1][y1] == 1, isLeaf=True)
            
            midX, midY = (x1 + x2) // 2, (y1 + y2) // 2
            
            topLeft = buildQuadTree(x1, y1, midX, midY)
            topRight = buildQuadTree(x1, midY, midX, y2)
            bottomLeft = buildQuadTree(midX, y1, x2, midY)
            bottomRight = buildQuadTree(midX, midY, x2, y2)
            
            return Node(val=True, isLeaf=False, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)
        
        n = len(grid)
        return buildQuadTree(0, 0, n, n)
