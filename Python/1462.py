class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize a matrix where isPrerequisite[i][j] means "i is a prerequisite of j"
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        # Set the direct prerequisites
        for pre in prerequisites:
            isPrerequisite[pre[0]][pre[1]] = True
        
        # Floyd-Warshall algorithm to compute the transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if isPrerequisite[i][k] and isPrerequisite[k][j]:
                        isPrerequisite[i][j] = True
        
        # Answer the queries by checking if u is a prerequisite of v
        return [isPrerequisite[u][v] for u, v in queries]
