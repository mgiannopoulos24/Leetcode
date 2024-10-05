class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0
        
        for num in pushed:
            stack.append(num)  # Push element onto stack
            
            # Check if top of stack matches the current element in popped
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        
        # If stack is empty, all elements matched correctly
        return not stack
