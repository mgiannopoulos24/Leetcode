class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n  # Initialize the answer array
        stack = []  # Monotonic stack to keep heights in decreasing order
        
        # Iterate from the end to the start
        for i in range(n - 1, -1, -1):
            count = 0  # Number of people the current person can see
            
            # Pop elements from the stack that are shorter than the current person's height
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            
            # If the stack is not empty, the current person can also see the person at the top of the stack
            if stack:
                count += 1
            
            # Record the result
            answer[i] = count
            
            # Push the current person's height onto the stack
            stack.append(heights[i])
        
        return answer