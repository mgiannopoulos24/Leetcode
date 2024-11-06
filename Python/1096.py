class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def union(sets):
            result = set()
            for s in sets:
                result |= s  # Union of sets
            return result

        def concatenate(set1, set2):
            if not set1:
                return set2
            if not set2:
                return set1
            return {a + b for a in set1 for b in set2}
        
        stack = []
        current_set = set()
        temp_set = set()
        i = 0
        while i < len(expression):
            if expression[i].isalpha():
                # Handle individual letters
                temp_set = {expression[i]}
                if current_set:
                    current_set = concatenate(current_set, temp_set)
                else:
                    current_set = temp_set
            elif expression[i] == '{':
                # Push the current state onto the stack and start a new one
                stack.append(current_set)
                stack.append('union')  # Push 'union' as a marker
                current_set = set()
            elif expression[i] == '}':
                # Pop and process the union of all sets inside the braces
                while stack and stack[-1] != 'union':
                    current_set = union([stack.pop(), current_set])
                stack.pop()  # Pop the 'union' marker
                if stack and isinstance(stack[-1], set):
                    # Handle concatenation with the previous state on the stack
                    prev_set = stack.pop()
                    current_set = concatenate(prev_set, current_set)
            elif expression[i] == ',':
                # Push the current set onto the stack as part of a union
                stack.append(current_set)
                current_set = set()
            i += 1
        
        # Final result
        result = union([current_set] + [s for s in stack if isinstance(s, set)])
        return sorted(result)
